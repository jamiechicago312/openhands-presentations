# OpenHands Presentations

AI-powered presentation factory using Marp. Each branch is a presentation, main branch holds templates.

## 🚀 Quick Start

### Create a New Presentation

```bash
# Create a new branch for your presentation
git checkout -b presentation/q4-sales

# Edit slides.md with your content
# Push to trigger auto-build
git add slides.md
git commit -m "Add Q4 sales deck"
git push -u origin presentation/q4-sales
```

### Download Your Presentation

1. Go to **Actions** tab in GitHub
2. Click on your workflow run
3. Download `presentation-output` artifact
4. Extract to get `slides.pptx` and `slides.pdf`

## 📁 Repository Structure

```
main branch (template)
├── .github/workflows/
│   └── build-slides.yml      # Auto-builds PPTX on push
├── themes/
│   ├── default.css           # Your custom theme
│   ├── minimal.css           # Alternative minimal theme
│   └── backgrounds/          # Background images
├── utils/
│   └── extract-from-pptx.py  # Extract design from existing PPTX
├── template.md               # Example presentation
└── README.md                 # This file

presentation/* branches (your decks)
└── slides.md                 # Your actual presentation content
```

## 🎨 Using the Template

### Basic Slide Structure

```markdown
---
marp: true
theme: default
paginate: true
---

# Main Title
## Subtitle

---

## Slide with Bullets

- Point 1
- Point 2
- Point 3

---

## Two Column Layout

<div class="columns">
<div>

### Left Column
Content here

</div>
<div>

### Right Column
More content

</div>
</div>

---

![bg](themes/backgrounds/background.png)

# Full Background Image

---

## Image in Slide

![width:600px](path/to/image.png)
```

## 🎨 Customizing the Theme

Edit `themes/default.css` to modify:
- Colors
- Fonts
- Background images
- Layouts

## 📤 Importing to Google Slides

1. Download the `slides.pptx` from GitHub Actions artifacts
2. Upload to Google Drive
3. Right-click → "Open with Google Slides"
4. It will auto-convert (most formatting preserved)

## 🔧 Extracting Design from Existing PPTX

If you have an existing PowerPoint template:

```bash
python utils/extract-from-pptx.py your-template.pptx
```

This will:
- Extract background images
- Identify color scheme
- Detect fonts used
- Generate a matching Marp theme

## 📝 Best Practices

### Font Sizes (Accessibility)
- **Title**: 44pt minimum
- **Headings**: 32pt minimum  
- **Body text**: 24pt minimum
- **Captions**: 18pt minimum

### Content
- Max 6 bullets per slide
- Max 6 words per bullet
- Use high contrast colors (4.5:1 minimum)
- Include alt text for images

## 🤖 AI Workflow

When working with AI agents (like me!):

1. **Tell me your topic**: "Create a presentation about Q4 sales results"
2. **I'll write the `slides.md`** in proper Marp format
3. **Push and download**: GitHub Actions builds it automatically
4. **Iterate**: Just update `slides.md` and push again

## 🔄 Reverse Conversion

Convert existing PPTX to Marp Markdown:

```bash
# Install pandoc first
sudo apt-get update && sudo apt-get install -y pandoc

# Convert
pandoc your-presentation.pptx -o slides.md
```

Note: This extracts content but loses complex layouts. You'll need to adjust formatting.

## 📋 Common Workflows

### Personal Template Library
```bash
main → themes/corporate.css
main → themes/sales.css  
main → themes/minimal.css
```

### Project-Specific Presentations
```bash
git checkout -b presentation/project-kickoff
git checkout -b presentation/milestone-1
git checkout -b presentation/final-review
```

## 🆘 Troubleshooting

**Actions failing?**
- Check `.github/workflows/build-slides.yml` exists
- Verify `slides.md` has `---\nmarp: true\n---` at the top

**Theme not applying?**
- Check theme filename matches `theme: default` in slides.md frontmatter
- Verify CSS file is in `themes/` directory

**Fonts not showing?**
- Marp supports: system fonts, Google Fonts (via CSS imports)
- For custom fonts, include @font-face in theme CSS

## 📚 Resources

- [Marp Documentation](https://marpit.marp.app/)
- [Marp CLI](https://github.com/marp-team/marp-cli)
- [Theme Examples](https://github.com/marp-team/marp-core/tree/main/themes)
