#!/usr/bin/env bash
# setup_tex_user_tree.sh — install the LaTeX packages the book build needs
# into the user texmf tree (~/texmf), without root/sudo.
#
# The build machine's distro TeX Live lacks texlive-luatex and a few other
# packages (no xelatex either). This script installs, per package only when
# missing:
#   luaotfload   (GitHub release TDS zip)      — OTF/TTF font loading for LuaTeX
#   lualibs      (GitHub source + docstrip)    — luaotfload dependency
#   lua-uni-algos (CTAN)                       — luaotfload dependency
#   lualatex-math (CTAN, docstrip)             — required by unicode-math
#   luatexbase   (CTAN zip, docstrip)          — required by babel-vietnamese
#   ctablestack  (CTAN, docstrip)              — required by babel-vietnamese
#   selnolig     (CTAN)                        — loaded by pandoc under LuaTeX
#
# Fonts: no font binaries are vendored. The build uses system fonts with
# full Vietnamese coverage (DejaVu Serif/Sans/Mono on this machine; see
# book/header.tex). Install fonts-dejavu (or any Vietnamese-capable font
# family) and adjust book/header.tex if needed.
#
# Usage: scripts/setup_tex_user_tree.sh
set -euo pipefail

TEXMFHOME="$(kpsewhich -var-value TEXMFHOME)"
CTAN="https://mirrors.ctan.org"
GH="https://github.com"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

have() { kpsewhich "$1" >/dev/null 2>&1; }

fetch() { # fetch <url> <dest>
  curl -sL --retry 3 --max-time 300 -o "$2" "$1"
  [ -s "$2" ] || { echo "setup_tex: download failed: $1" >&2; exit 1; }
}

# --- luaotfload -------------------------------------------------------------
if ! have luaotfload.sty; then
  echo "setup_tex: installing luaotfload"
  fetch "$GH/latex3/luaotfload/releases/download/v3.29/luaotfload.tds.zip" "$WORK/luaotfload.tds.zip"
  (cd "$TEXMFHOME" && unzip -oq "$WORK/luaotfload.tds.zip")
fi

# --- lualibs ----------------------------------------------------------------
if ! have lualibs.lua; then
  echo "setup_tex: installing lualibs"
  fetch "$GH/latex3/lualibs/archive/refs/heads/main.zip" "$WORK/lualibs.zip"
  (cd "$WORK" && unzip -oq lualibs.zip && cd lualibs-main && tex lualibs.dtx </dev/null >/dev/null)
  mkdir -p "$TEXMFHOME/tex/luatex/lualibs"
  cp "$WORK"/lualibs-main/*.lua "$TEXMFHOME/tex/luatex/lualibs/"
fi

# --- lua-uni-algos ----------------------------------------------------------
if ! have lua-uni-case.lua; then
  echo "setup_tex: installing lua-uni-algos"
  mkdir -p "$TEXMFHOME/tex/luatex/lua-uni-algos"
  for f in lua-uni-algos.lua lua-uni-case.lua lua-uni-data-parser.lua \
           lua-uni-data-preload.lua lua-uni-data.lua lua-uni-graphemes.lua \
           lua-uni-normalize.lua lua-uni-parse.lua lua-uni-stage-tables.lua \
           lua-uni-words.lua; do
    fetch "$CTAN/macros/luatex/generic/lua-uni-algos/$f" \
          "$TEXMFHOME/tex/luatex/lua-uni-algos/$f"
  done
fi

# --- lualatex-math ----------------------------------------------------------
if ! have lualatex-math.sty; then
  echo "setup_tex: installing lualatex-math"
  mkdir -p "$WORK/lualatex-math"
  fetch "$CTAN/macros/luatex/latex/lualatex-math/lualatex-math.dtx" "$WORK/lualatex-math/lualatex-math.dtx"
  fetch "$CTAN/macros/luatex/latex/lualatex-math/lualatex-math.ins" "$WORK/lualatex-math/lualatex-math.ins"
  (cd "$WORK/lualatex-math" && tex lualatex-math.ins </dev/null >/dev/null)
  mkdir -p "$TEXMFHOME/tex/latex/lualatex-math" "$TEXMFHOME/tex/luatex/lualatex-math"
  cp "$WORK/lualatex-math/lualatex-math.sty" "$TEXMFHOME/tex/latex/lualatex-math/"
  cp "$WORK/lualatex-math/lualatex-math.lua" "$TEXMFHOME/tex/luatex/lualatex-math/"
fi

# --- luatexbase -------------------------------------------------------------
if ! have luatexbase.sty; then
  echo "setup_tex: installing luatexbase"
  fetch "$CTAN/macros/luatex/generic/luatexbase.zip" "$WORK/luatexbase.zip"
  (cd "$WORK" && unzip -oq luatexbase.zip && cd luatexbase && tex luatexbase.ins </dev/null >/dev/null)
  mkdir -p "$TEXMFHOME/tex/latex/luatexbase"
  cp "$WORK"/luatexbase/*.sty "$TEXMFHOME/tex/latex/luatexbase/"
fi

# --- ctablestack ------------------------------------------------------------
if ! have ctablestack.sty; then
  echo "setup_tex: installing ctablestack"
  mkdir -p "$WORK/ctablestack"
  fetch "$CTAN/macros/luatex/generic/ctablestack/ctablestack.dtx" "$WORK/ctablestack/ctablestack.dtx"
  fetch "$CTAN/macros/luatex/generic/ctablestack/ctablestack.ins" "$WORK/ctablestack/ctablestack.ins"
  (cd "$WORK/ctablestack" && tex ctablestack.ins </dev/null >/dev/null)
  mkdir -p "$TEXMFHOME/tex/latex/ctablestack"
  cp "$WORK/ctablestack/ctablestack.sty" "$TEXMFHOME/tex/latex/ctablestack/"
fi

# --- selnolig ---------------------------------------------------------------
if ! have selnolig.sty; then
  echo "setup_tex: installing selnolig"
  mkdir -p "$TEXMFHOME/tex/latex/selnolig"
  for f in selnolig.sty selnolig.lua selnolig-english-patterns.sty \
           selnolig-english-hyphex.sty gpp-ft.fea; do
    fetch "$CTAN/macros/luatex/latex/selnolig/$f" "$TEXMFHOME/tex/latex/selnolig/$f"
  done
fi

mktexlsr "$TEXMFHOME" >/dev/null 2>&1 || true
echo "setup_tex: done"
