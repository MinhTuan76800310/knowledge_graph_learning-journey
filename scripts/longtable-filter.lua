-- longtable-filter.lua — Force all tables to use longtable environment in LaTeX.
-- This prevents tall tables from overflowing the page and causing text overlap.
--
-- Also replaces Unicode symbols that Times New Roman lacks with LaTeX
-- equivalents so they render via the math font (no font subsetting issues).
--
-- Usage: pandoc --lua-filter=scripts/longtable-filter.lua ...

local SYMBOL_MAP = {
  ["★"] = "\\ding{72}",
  ["⚠"] = "\\ding{43}",
  ["⚑"] = "\\ding{91}",
  ["□"] = "\\ensuremath{\\square}",
  ["✓"] = "\\ding{51}",
  ["✗"] = "\\ding{55}",
  ["📦"] = "\\ding{118}",
  ["🖊"] = "\\ding{46}",
  ["📐"] = "\\ding{118}",
  ["↦"] = "\\ensuremath{\\mapsto}",
  ["⊆"] = "\\ensuremath{\\subseteq}",
  ["⊑"] = "\\ensuremath{\\sqsubseteq}",
  ["∈"] = "\\ensuremath{\\in}",
  ["×"] = "\\ensuremath{\\times}",
  ["≠"] = "\\ensuremath{\\neq}",
  ["→"] = "\\ensuremath{\\rightarrow}",
  ["λ"] = "\\ensuremath{\\lambda}",
}

local function replace_symbols(s)
  for unicode_char, latex_cmd in pairs(SYMBOL_MAP) do
    s = s:gsub(unicode_char, latex_cmd)
  end
  return s
end

function Str(el)
  if FORMAT:match("latex") then
    local replaced = replace_symbols(el.text)
    if replaced ~= el.text then
      return pandoc.RawInline("latex", replaced)
    end
  end
  return el
end

function Code(el)
  if FORMAT:match("latex") then
    local replaced = replace_symbols(el.text)
    if replaced ~= el.text then
      -- Wrap in \texttt{} so the LaTeX commands render in monospace context
      return pandoc.RawInline("latex", "\\texttt{" .. replaced .. "}")
    end
  end
  return el
end

function Table(tbl)
  if FORMAT:match("latex") then
    tbl.attr = tbl.attr or {}
    local classes = tbl.attr.classes or {}
    local has_longtable = false
    for _, cls in ipairs(classes) do
      if cls == "longtable" then
        has_longtable = true
        break
      end
    end
    if not has_longtable then
      classes[#classes + 1] = "longtable"
      tbl.attr.classes = classes
    end
  end
  return tbl
end
