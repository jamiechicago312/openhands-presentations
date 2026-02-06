# Theme Guide - OpenHands Extracted Theme

Complete guide to using your extracted PowerPoint theme in Marp presentations.

## 🎨 Theme Overview

**Theme Name**: `extracted`  
**Based On**: Your PowerPoint template  
**Typography**: Inter font family  
**Color Scheme**: Minimalist with blue accents  
**Backgrounds**: Beige/cream with geometric patterns  

## 📐 Design System

### Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Dark Gray | `#212121` | Headings, body text |
| Blue Accent | `#4285f4` | Emphasis, links, highlights |
| Beige | `#f5f5f0` | Background color |
| Medium Gray | `#595959` | Secondary text |
| White | `#ffffff` | Text on dark backgrounds |

### Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Title Slide H1 | Inter | 68pt | 700 Bold |
| Section H1 | Inter | 56pt | 700 Bold |
| Section H2 | Inter | 38pt | 600 SemiBold |
| Section H3 | Inter | 32pt | 600 SemiBold |
| Body Text | Inter | 26pt | 400 Regular |
| Small Text | Inter | 20pt | 400 Regular |

**✅ All sizes meet WCAG accessibility standards**

### Spacing

- Slide padding: 70px (top/bottom), 90px (left/right)
- Line height: 1.5 for body, 1.2 for headings
- List item spacing: 0.6em between items

## 🚀 Quick Start

### Basic Setup

```markdown
---
marp: true
theme: extracted
paginate: true
---
```

### Title Slide

```markdown
<!-- _class: title -->
<!-- _paginate: false -->

# Main Title
## Subtitle or Tagline

Your Name · Date
```

### Content Slide

```markdown
---

## Slide Heading

Regular paragraph text with **bold emphasis** and *blue emphasis*.

- Bullet point 1
- Bullet point 2
- Bullet point 3
```

## 🎯 Background Options

### Default Background (Beige with Patterns)

```markdown
---

## Your Content

This automatically uses image15.png background
```

### Yellow Background

```markdown
<!-- _class: bg-yellow -->

## Your Content

Uses the yellow geometric pattern background
```

### Plain Background (No Pattern)

```markdown
<!-- _class: bg-plain -->

## Your Content

Solid beige color, no geometric patterns
```

### Custom Background Image

```markdown
![bg](themes/backgrounds/image5.png)

## Your Content
```

## 📋 Layout Options

### Centered Content

```markdown
<!-- _class: center -->

## Centered Heading

Vertically and horizontally centered content
```

### Two Columns

```markdown
<div class="columns">
<div>

### Left Column
Content here

</div>
<div>

### Right Column
Content here

</div>
</div>
```

### Three Columns

```markdown
<div class="columns-3">
<div>

Column 1

</div>
<div>

Column 2

</div>
<div>

Column 3

</div>
</div>
```

## 💡 Special Elements

### Highlight Boxes

**Info Box (Blue)**
```markdown
<div class="highlight info">

💡 **Pro Tip**: Your information here

</div>
```

**Success Box (Green)**
```markdown
<div class="highlight success">

✅ **Done**: Success message

</div>
```

**Warning Box (Yellow)**
```markdown
<div class="highlight warning">

⚠️ **Note**: Important warning

</div>
```

**Danger Box (Red)**
```markdown
<div class="highlight danger">

🚨 **Alert**: Critical information

</div>
```

### Blockquotes

```markdown
> "This is a quote or testimonial"
> 
> — Attribution Name
```

### Code Blocks

**Inline code**: Use `backticks`

**Code block**:
````markdown
```python
def hello():
    return "world"
```
````

### Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Data A | Data B | Data C |
| Data D | Data E | Data F |
```

### Lists with Icons

```markdown
- 🎯 **Goal** - Description
- 📊 **Data** - Description
- 🚀 **Action** - Description
```

## 🎨 Text Styling

### Emphasis

- **Bold text** → `**bold**` (dark gray, weight 600)
- *Emphasis* → `*emphasis*` (blue accent, weight 500)
- ***Both*** → `***both***`

### Links

```markdown
[Link text](https://example.com)
```

Links appear in blue with underline.

### Text Utilities

```markdown
<p class="text-large">Larger text</p>
<p class="text-small">Smaller text</p>
<p class="text-muted">Muted gray text</p>
<p class="text-center">Centered text</p>
```

## 📄 Complete Example

```markdown
---
marp: true
theme: extracted
paginate: true
header: 'Company Name'
footer: 'Confidential'
---

<!-- _class: title -->
<!-- _paginate: false -->

# Quarterly Review
## Q1 2024 Results

Jane Doe · Marketing Director

---

## Agenda

1. **Overview** - Key highlights
2. **Metrics** - Performance data
3. **Insights** - What we learned
4. **Next Steps** - Q2 planning

---

## Key Highlights

<div class="highlight success">

✅ **Achievement**: Exceeded targets by 25%

</div>

- Revenue growth: **$2.1M** (+30% QoQ)
- New customers: **1,200** (+45% QoQ)
- Customer satisfaction: **4.8/5** ⭐

---

<div class="columns">
<div>

## Wins

- Product launch success
- Strong customer retention
- Team expansion

</div>
<div>

## Challenges

- Supply chain delays
- Market competition
- Resource constraints

</div>
</div>

---

<!-- _class: bg-yellow -->

## Q2 Focus Areas

1. 🎯 **Expand** - New market segments
2. 📊 **Optimize** - Operational efficiency
3. 🚀 **Innovate** - Product enhancements

---

<!-- _class: center -->

## Questions?

jane.doe@company.com
```

## 🛠️ Customization Tips

### Adjust Colors

Edit `themes/extracted.css`:

```css
:root {
  --color-primary: #212121;     /* Change heading color */
  --color-accent: #4285f4;      /* Change accent color */
  --color-background: #f5f5f0;  /* Change background */
}
```

### Change Default Background

```css
section {
  background-image: url('./backgrounds/image20.png');
}
```

### Adjust Font Sizes

```css
:root {
  --font-size-body: 28pt;  /* Increase body text */
  --font-size-heading: 40pt;  /* Larger headings */
}
```

## 📚 Resources

- [Marp Documentation](https://marpit.marp.app/)
- [Marp CLI](https://github.com/marp-team/marp-cli)
- [Inter Font](https://fonts.google.com/specimen/Inter)

## 🎯 Best Practices

1. **Keep it simple** - Max 6 bullets per slide
2. **Use hierarchy** - Clear heading structure
3. **Consistent spacing** - Don't overcrowd slides
4. **High contrast** - Dark text on light backgrounds
5. **Visual breaks** - Use different layouts to maintain interest
6. **Test export** - Always check PPTX output before sharing

## 🚀 AI Workflow

When working with AI (like me!):

**Prompt Example**:
```
Create a 10-slide presentation about "Digital Transformation" 
using the extracted theme. Include:
- Title slide
- Agenda
- 3 main sections with 2 slides each
- One slide with two-column layout
- Summary with highlight boxes
- Q&A slide
```

I'll generate properly formatted Markdown that looks perfect in your brand!
