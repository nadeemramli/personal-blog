---
title: Canvas Documentation
draft: false
tags: #development
---

# Canvas Integration

The Canvas component allows you to embed Obsidian Canvas visualizations into your Quartz site. This feature uses exported canvas files from Obsidian's Web Export plugin to render interactive canvas views.

## Setup

1. Install the required Obsidian plugin:
   - Install "Webpage HTML Export" plugin in Obsidian
   - Enable the plugin

2. Export your canvas:
   - Open the plugin and click all the canvas you want to export. (If you want to add more canvas, you have to "re-export" all the canvas, cause the lib folder can only have one.)
   - Use the "Online Web Serve" export mode command
   - Save the exported files to your `content/Canvas` directory
   - Replace the previous lib folder with the new one.
   - Ensure all html files are in the `html` folder, or their respective folder.

3. The component is already configured in your Quartz layout:
   - Located in `quartz/components/Canvas.tsx`
   - Integrated into the default page layout.
   - Update the `canvasPath` in the component to match your canvas file structure.

## Relevant Files

The Component:
- `quartz.layout.tsx`
- `quartz/components/Canvas.tsx`
- `quartz/content/canvases.md`

The Canvas:
- `content/Canvas/lib/metadata.json`
- `content/Canvas/html/your-canvas-name.html`

## Usage

1. Create a canvas file in Obsidian and design your visualization

2. Export the canvas:   ```bash
   content/
   ├── Canvas/
   │   ├── html/
   │   │   └── your-canvas-name.html
   │   └── lib/
   │       ├── scripts/
   │       ├── styles/
   │       └── other assets...   ```

3. Create or update your canvas index page:   ```markdown
   ---
   title: Canvases
   draft: false
   ---

   This page contains all canvas visualizations.   ```

4. The Canvas component will automatically:
   - Only render on pages within the "canvases" path
   - Check for draft status before rendering
   - Handle loading states and iframe integration

## Component Details

The Canvas component provides:
- Responsive container sizing
- Loading indicator
- Automatic iframe cleanup
- Mobile-friendly layout

### Styling

The canvas is styled with:
- 16:9 aspect ratio
- Rounded corners
- Subtle shadow
- Responsive width
- Custom loading indicator

## Troubleshooting

Common issues:
1. Canvas not showing
   - Ensure the file path is correct
   - Verify the page is not marked as draft
   - Check that the page URL includes "canvases"

2. Loading issues
   - Confirm all exported files are in the correct directory
   - Verify the HTML file path matches your configuration