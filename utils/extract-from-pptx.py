#!/usr/bin/env python3
"""
Extract design elements from a PowerPoint file to create a Marp theme.

Usage:
    python extract-from-pptx.py your-template.pptx

This will:
- Extract background images from slides
- Identify color scheme used
- Detect font families
- Generate a custom Marp CSS theme
"""

import sys
import os
from pathlib import Path
from collections import Counter
import zipfile
import xml.etree.ElementTree as ET
import shutil


def rgb_to_hex(r, g, b):
    """Convert RGB values to hex color code."""
    return f"#{r:02x}{g:02x}{b:02x}"


def extract_backgrounds(pptx_path, output_dir="themes/backgrounds"):
    """Extract background images from PPTX file."""
    print(f"📂 Extracting backgrounds from {pptx_path}...")
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    backgrounds = []
    
    try:
        with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
            # Extract media files (images)
            for file_info in zip_ref.filelist:
                if file_info.filename.startswith('ppt/media/'):
                    filename = os.path.basename(file_info.filename)
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        # Extract to backgrounds folder
                        target_path = output_path / filename
                        with zip_ref.open(file_info.filename) as source:
                            with open(target_path, 'wb') as target:
                                shutil.copyfileobj(source, target)
                        backgrounds.append(filename)
                        print(f"  ✓ Extracted: {filename}")
    
    except Exception as e:
        print(f"  ⚠️  Error extracting backgrounds: {e}")
    
    return backgrounds


def extract_colors(pptx_path):
    """Extract color scheme from PPTX file."""
    print(f"🎨 Analyzing color scheme...")
    
    colors = []
    
    try:
        with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
            # Read theme colors from theme XML
            for file_info in zip_ref.filelist:
                if 'theme/theme' in file_info.filename and file_info.filename.endswith('.xml'):
                    with zip_ref.open(file_info.filename) as f:
                        tree = ET.parse(f)
                        root = tree.getroot()
                        
                        # Find color scheme elements
                        namespaces = {
                            'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'
                        }
                        
                        for color_elem in root.findall('.//a:srgbClr', namespaces):
                            val = color_elem.get('val')
                            if val:
                                colors.append(f"#{val.lower()}")
                        
                        for sys_color in root.findall('.//a:sysClr', namespaces):
                            last_clr = sys_color.get('lastClr')
                            if last_clr:
                                colors.append(f"#{last_clr.lower()}")
    
    except Exception as e:
        print(f"  ⚠️  Could not extract colors: {e}")
    
    # Remove duplicates and most common
    unique_colors = list(dict.fromkeys(colors))
    
    if unique_colors:
        print(f"  ✓ Found {len(unique_colors)} unique colors")
        for i, color in enumerate(unique_colors[:6], 1):
            print(f"    {i}. {color}")
    else:
        print("  ⚠️  No colors found, using defaults")
        unique_colors = ["#2563eb", "#7c3aed", "#0ea5e9", "#1e293b", "#64748b"]
    
    return unique_colors


def extract_fonts(pptx_path):
    """Extract font families used in PPTX."""
    print(f"🔤 Analyzing fonts...")
    
    fonts = []
    
    try:
        with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
            # Read fonts from slide XML files
            for file_info in zip_ref.filelist:
                if file_info.filename.startswith('ppt/slides/slide') and file_info.filename.endswith('.xml'):
                    with zip_ref.open(file_info.filename) as f:
                        content = f.read().decode('utf-8', errors='ignore')
                        
                        # Simple regex-like search for font names
                        # Look for typeface attributes
                        if 'typeface=' in content:
                            parts = content.split('typeface="')
                            for part in parts[1:]:
                                font_name = part.split('"')[0]
                                if font_name and not font_name.startswith('+'):
                                    fonts.append(font_name)
    
    except Exception as e:
        print(f"  ⚠️  Could not extract fonts: {e}")
    
    if fonts:
        # Count font usage
        font_counter = Counter(fonts)
        most_common = font_counter.most_common(5)
        
        print(f"  ✓ Found {len(font_counter)} unique fonts")
        print("  📊 Most used:")
        for font, count in most_common:
            print(f"    • {font} ({count} times)")
        
        return [font for font, _ in most_common]
    else:
        print("  ⚠️  No fonts found, using system defaults")
        return ["Segoe UI", "Arial", "Helvetica"]


def generate_marp_theme(colors, fonts, backgrounds, output_path="themes/extracted.css"):
    """Generate a Marp CSS theme from extracted design elements."""
    print(f"\n📝 Generating Marp theme...")
    
    # Pick primary colors
    primary = colors[0] if len(colors) > 0 else "#2563eb"
    secondary = colors[1] if len(colors) > 1 else "#7c3aed"
    accent = colors[2] if len(colors) > 2 else "#0ea5e9"
    text_dark = colors[3] if len(colors) > 3 else "#1e293b"
    text_light = colors[4] if len(colors) > 4 else "#64748b"
    
    # Pick primary font
    primary_font = fonts[0] if fonts else "Segoe UI"
    
    # Background image reference
    bg_image = f"./backgrounds/{backgrounds[0]}" if backgrounds else ""
    
    css_content = f"""/*
 * Extracted Theme - Generated from your PowerPoint template
 * 
 * Colors and fonts extracted from: source PPTX
 * Follows accessibility best practices for font sizes.
 */

/* @theme extracted */

@import 'default';

:root {{
  /* Extracted Color Palette */
  --color-primary: {primary};
  --color-secondary: {secondary};
  --color-background: #ffffff;
  --color-text: {text_dark};
  --color-text-light: {text_light};
  --color-accent: {accent};
  
  /* Extracted Typography */
  --font-family-sans: '{primary_font}', 'Segoe UI', Roboto, sans-serif;
  --font-family-serif: Georgia, 'Times New Roman', serif;
  --font-family-mono: 'Courier New', monospace;
  
  /* Font Sizes - Best Practices */
  --font-size-title: 54pt;
  --font-size-heading: 36pt;
  --font-size-body: 28pt;
  --font-size-small: 20pt;
}}

section {{
  background-color: var(--color-background);
  color: var(--color-text);
  font-family: var(--font-family-sans);
  font-size: var(--font-size-body);
  padding: 80px;
"""
    
    if bg_image:
        css_content += f"""  
  /* Background from your template */
  background-image: url('{bg_image}');
  background-size: cover;
  background-position: center;
"""
    
    css_content += """
}

/* Apply your colors to headings */
h1 {
  font-size: var(--font-size-title);
  color: var(--color-primary);
  font-weight: 700;
}

h2 {
  font-size: var(--font-size-heading);
  color: var(--color-primary);
  font-weight: 600;
}

h3 {
  font-size: 30pt;
  color: var(--color-secondary);
  font-weight: 600;
}

/* Style links and emphasis with your colors */
strong {
  color: var(--color-primary);
}

em {
  color: var(--color-secondary);
}

a {
  color: var(--color-accent);
}
"""
    
    # Write theme file
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output, 'w') as f:
        f.write(css_content)
    
    print(f"  ✓ Theme saved to: {output}")
    print(f"\n✅ Done! Use this theme in your slides.md:")
    print(f"   ---")
    print(f"   marp: true")
    print(f"   theme: extracted")
    print(f"   ---")


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract-from-pptx.py <your-template.pptx>")
        print("\nExample:")
        print("  python extract-from-pptx.py ~/Downloads/template.pptx")
        sys.exit(1)
    
    pptx_path = sys.argv[1]
    
    if not os.path.exists(pptx_path):
        print(f"❌ Error: File not found: {pptx_path}")
        sys.exit(1)
    
    print("=" * 60)
    print("🎨 PowerPoint Design Extractor for Marp")
    print("=" * 60)
    print()
    
    # Extract design elements
    backgrounds = extract_backgrounds(pptx_path)
    colors = extract_colors(pptx_path)
    fonts = extract_fonts(pptx_path)
    
    # Generate Marp theme
    generate_marp_theme(colors, fonts, backgrounds)
    
    print("\n" + "=" * 60)
    print("✨ Next steps:")
    print("  1. Review themes/extracted.css")
    print("  2. Adjust colors/fonts as needed")
    print("  3. Create slides.md with theme: extracted")
    print("  4. Push to build your presentation!")
    print("=" * 60)


if __name__ == "__main__":
    main()
