# Upload Your PowerPoint Template

Follow these steps to extract design elements from your existing PowerPoint template.

## Step 1: Upload Your PPTX

Upload your PowerPoint template file to this repository:

### Option A: Via Git (Local)
```bash
# Clone the repo if you haven't already
git clone https://github.com/jamiechicago312/openhands-presentations.git
cd openhands-presentations

# Copy your template file
cp ~/path/to/your-template.pptx ./template-source.pptx

# Run the extractor
python3 utils/extract-from-pptx.py template-source.pptx
```

### Option B: Via GitHub Web Interface
1. Go to https://github.com/jamiechicago312/openhands-presentations
2. Click "Add file" → "Upload files"
3. Drag your PPTX file
4. Commit with message: "Add PowerPoint template"

Then run extraction via GitHub Codespaces or locally.

## Step 2: Extract Design Elements

Run the extraction script:

```bash
python3 utils/extract-from-pptx.py template-source.pptx
```

This will:
- ✅ Extract all background images to `themes/backgrounds/`
- ✅ Analyze colors used in the template
- ✅ Detect font families
- ✅ Generate `themes/extracted.css` with your brand styling

## Step 3: Review and Adjust

1. **Check backgrounds**: Look in `themes/backgrounds/` for extracted images
2. **Review theme**: Open `themes/extracted.css` and adjust colors/fonts if needed
3. **Test template**: Create a test slide deck:

```bash
cp template.md slides.md
# Edit slides.md and change:
# theme: default
# to:
# theme: extracted
```

## Step 4: Commit Changes

```bash
git add themes/
git commit -m "Add extracted theme from PowerPoint template"
git push
```

## What Gets Extracted

### ✅ Successfully Extracted
- Background images (PNG, JPG, GIF)
- Color scheme from theme definitions
- Font families used in slides
- Basic layout structure

### ⚠️ May Need Manual Adjustment
- Exact font sizes (we apply best practices)
- Complex gradients (simplified to solid colors)
- Custom shapes (not supported in Marp)
- Animations (not applicable to Marp)

## Troubleshooting

### "No backgrounds extracted"
- Your PPTX might use solid colors instead of images
- You can manually add backgrounds to `themes/backgrounds/`

### "Colors look different"
- PowerPoint uses theme colors that may render differently
- Manually adjust RGB values in `themes/extracted.css`

### "Fonts not matching"
- Marp uses web-safe fonts
- If your template uses custom fonts:
  1. Find web font alternatives (Google Fonts)
  2. Add `@import` statement to CSS
  3. Update `--font-family-sans` variable

## Example Workflow

```bash
# 1. Upload template
cp ~/Downloads/company-template.pptx ./

# 2. Extract design
python3 utils/extract-from-pptx.py company-template.pptx

# 3. Review output
ls themes/backgrounds/
cat themes/extracted.css

# 4. Test with template
cp template.md slides.md
# Edit slides.md: change theme to "extracted"

# 5. Commit
git add themes/ slides.md
git commit -m "Extract design from company template"
git push

# 6. Check Actions tab for built PPTX
```

## Need Help?

If the extraction doesn't work perfectly:
1. Share the template PPTX with your AI assistant
2. Manually describe the colors and fonts
3. We'll hand-craft the perfect Marp theme for you!

The goal is to get 80% automated, then fine-tune the last 20% manually.
