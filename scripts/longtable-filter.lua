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
  ["✅"] = "\\ding{51}",
  ["❌"] = "\\ding{55}",
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

-- Split a string on the earliest occurrence of any mapped symbol.
-- Returns the plain prefix and the symbol + its replacement command, or
-- (nil, nil, nil) when the string contains no mapped symbol.
local function split_symbol(s)
  local idx, len, cmd
  for ch, c in pairs(SYMBOL_MAP) do
    local at = s:find(ch, 1, true)
    if at and (not idx or at < idx) then
      idx, len, cmd = at, #ch, c
    end
  end
  if not idx then
    return nil, nil, nil
  end
  return s:sub(1, idx - 1), s:sub(idx, idx + len - 1), cmd
end

-- Return the given inline elements (from a Str) or a Code span with the same
-- text, splitting out mapped symbols into RawInline LaTeX. Everything that is
-- not a mapped symbol stays a normal element so the LaTeX writer escapes it
-- correctly (e.g. underscores in RATE_OF_CHANGE become \_).
local function split_symbols_inlines(text)
  local out = {}
  local rest = text
  while rest and rest ~= "" do
    local prefix, sym, cmd = split_symbol(rest)
    if not sym then
      out[#out + 1] = pandoc.Str(rest)
      break
    end
    if prefix ~= "" then
      out[#out + 1] = pandoc.Str(prefix)
    end
    out[#out + 1] = pandoc.RawInline("latex", cmd)
    rest = rest:sub(#prefix + #sym + 1)
  end
  return out
end

function Str(el)
  if FORMAT:match("latex") then
    local out = split_symbols_inlines(el.text)
    if #out == 1 and out[1].t == "Str" and out[1].text == el.text then
      return el
    end
    return out
  end
  return el
end

function Code(el)
  if FORMAT:match("latex") then
    local parts = split_symbols_inlines(el.text)
    if #parts == 1 and parts[1].t == "Str" and parts[1].text == el.text then
      return el
    end
    local out = {}
    local plain = {}
    for _, part in ipairs(parts) do
      if part.t == "Str" then
        plain[#plain + 1] = part.text
      else
        if #plain > 0 then
          out[#out + 1] = pandoc.Code(table.concat(plain))
          plain = {}
        end
        out[#out + 1] = part
      end
    end
    if #plain > 0 then
      out[#out + 1] = pandoc.Code(table.concat(plain))
    end
    return out
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
