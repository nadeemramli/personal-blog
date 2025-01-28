import { QuartzComponentConstructor, QuartzComponentProps } from "./types"

function Canvas(props: QuartzComponentProps) {
  const { fileData } = props

  // Only render on the Canvases page
  if (!fileData.filePath?.includes("canvases")) {
    return null
  }

  // Only render if the file exists and is not a draft
  if (fileData.frontmatter?.draft) {
    return null
  }

  const canvasPath = `/Canvas/html/maps-of-meta-learning.html`

  return (
    <div class="canvas-container">
      <div class="canvas-loading">Loading canvas...</div>
      <iframe
        src={canvasPath}
        class="canvas-frame"
        title="Maps of Meta-Learning"
        loading="lazy"
        onLoad={(e) => {
          const parent = (e.target as HTMLIFrameElement).parentElement
          if (parent) {
            const loader = parent.querySelector(".canvas-loading")
            if (loader) {
              loader.remove()
            }
          }
        }}
      />
      <style>{`
        .canvas-container {
          width: 100%;
          position: relative;
          padding-bottom: 56.25%;
          height: 0;
          overflow: hidden;
          margin: 2rem 0;
          background: var(--background-primary);
        }

        .canvas-frame {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          border: none;
          border-radius: 8px;
          box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .canvas-loading {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          font-size: 1rem;
          color: var(--text-muted);
        }
      `}</style>
    </div>
  )
}

export default (() => Canvas) satisfies QuartzComponentConstructor
