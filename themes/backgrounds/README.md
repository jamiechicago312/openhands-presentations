# Backgrounds Directory

Place your background images here to use in presentations.

## Usage in Slides

### Full Background Image

```markdown
---

![bg](themes/backgrounds/your-image.png)

# Your Title Here

---
```

### Background with Opacity

```markdown
---

![bg opacity:0.3](themes/backgrounds/your-image.png)

# Content with Subtle Background

---
```

### Multiple Backgrounds (Split Screen)

```markdown
---

![bg left](themes/backgrounds/image1.png)
![bg right](themes/backgrounds/image2.png)

---
```

## Extracting from PowerPoint

If you have an existing PowerPoint template, extract backgrounds:

```bash
python utils/extract-from-pptx.py your-template.pptx
```

This will automatically save background images to this directory.

## Recommended Image Specs

- **Format**: PNG (for transparency) or JPG
- **Resolution**: 1920x1080 (16:9) or 2560x1440 (for high-DPI)
- **File Size**: Keep under 500KB for fast loading
- **Naming**: Use descriptive names like `corporate-blue-bg.png`

## Currently Available

- Place your extracted backgrounds here
- Reference them in `themes/*.css` files
