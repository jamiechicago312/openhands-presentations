# Quick Start Guide

Get your first presentation up and running in 5 minutes!

## 🎯 Goal

By the end of this guide, you'll have:
1. ✅ A working presentation template
2. ✅ GitHub Actions auto-building PPTX files
3. ✅ Your first AI-generated presentation

## 📋 Prerequisites

- A GitHub account
- Basic familiarity with Markdown (or just follow the template!)

## 🚀 Steps

### 1. Clone or Fork This Repo

```bash
git clone https://github.com/jamiechicago312/openhands-presentations.git
cd openhands-presentations
```

### 2. Create Your First Presentation

```bash
# Create a new branch for your presentation
git checkout -b presentation/my-first-deck

# Copy the template
cp template.md slides.md

# Edit slides.md with your content
# (Use any text editor)
```

### 3. Edit Your Presentation

Open `slides.md` and modify:

```markdown
---
marp: true
theme: default
paginate: true
---

# My First Presentation
## Created with Marp + AI

Your Name · Today's Date

---

## My Key Points

- Point 1
- Point 2  
- Point 3

---

## Thank You!
```

### 4. Push and Build

```bash
git add slides.md
git commit -m "Add my first presentation"
git push -u origin presentation/my-first-deck
```

### 5. Download Your Presentation

1. Go to your GitHub repo
2. Click **Actions** tab
3. Click on the latest workflow run
4. Scroll down to **Artifacts**
5. Download `presentation-output.zip`
6. Extract to get your `.pptx`, `.pdf`, and `.html` files!

## 🎨 Next Steps

### Add Your Brand Theme

1. Upload your PowerPoint template (see [UPLOAD_TEMPLATE.md](UPLOAD_TEMPLATE.md))
2. Run `python3 utils/extract-from-pptx.py your-template.pptx`
3. Use `theme: extracted` in your `slides.md`

### Create More Presentations

```bash
git checkout main
git checkout -b presentation/q4-review
cp template.md slides.md
# Edit and push!
```

### Import to Google Slides

1. Upload the `.pptx` to Google Drive
2. Right-click → "Open with Google Slides"
3. Edit in Google Slides if needed

## 🤖 AI Workflow (OpenHands)

If you're using OpenHands or another AI coding assistant:

1. **Tell the AI**: "Create a presentation about [topic]"
2. **AI creates**: The Markdown file with proper Marp formatting
3. **AI pushes**: Commits and pushes to a new branch
4. **You download**: Get the built PPTX from Actions

Example prompt:
```
Create a 10-slide presentation about "The Benefits of AI in Healthcare"
using the Marp template. Include an introduction, 3 main sections with 
2 slides each, and a conclusion. Push to a new branch.
```

## 📝 Pro Tips

1. **Keep it simple**: Start with the basic template and add complexity later
2. **Preview locally**: Install [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) to preview while editing
3. **One branch per deck**: This keeps presentations organized and versioned
4. **Main = templates**: Keep your themes and templates in main branch

## ❓ Troubleshooting

### "Workflow not running"
- Make sure `slides.md` exists in your branch
- Check that `.github/workflows/build-slides.yml` is in your repo

### "PPTX looks different than expected"
- Marp has specific formatting rules
- Review the [template.md](template.md) for examples
- Check your theme CSS file

### "Can't find the artifact"
- Wait for the workflow to complete (green checkmark)
- Click on the workflow run, scroll to bottom
- Artifacts expire after 90 days

## 🆘 Need Help?

1. Check the [README.md](README.md) for detailed docs
2. Look at [template.md](template.md) for formatting examples
3. Review [Marp documentation](https://marpit.marp.app/)
4. Ask your AI assistant for help!

---

**Ready to create something awesome?** 🚀

Start with `git checkout -b presentation/my-topic` and let's go!
