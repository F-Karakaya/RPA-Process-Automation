import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Styles
    layer_style = dict(facecolor='#f0f0f0', edgecolor='#999999', boxstyle='round,pad=0.5', alpha=0.5)
    component_style = dict(facecolor='#dae8fc', edgecolor='#6c8ebf', boxstyle='round,pad=0.5')
    ai_style = dict(facecolor='#d5e8d4', edgecolor='#82b366', boxstyle='round,pad=0.5')
    db_style = dict(facecolor='#ffe6cc', edgecolor='#d79b00', boxstyle='cylinder') # Cylinder unavailable in basic patches, stick to round
    
    # Layers
    ax.text(8, 8.5, 'RPA & AI Automation Architecture', fontsize=18, fontweight='bold', ha='center')
    
    # Input Layer
    ax.text(2, 7.5, 'Input Sources', fontsize=12, fontweight='bold', ha='center')
    ax.add_patch(patches.Rectangle((0.5, 4), 3, 3, facecolor='#eeeeee', edgecolor='gray', alpha=0.3))
    ax.text(2, 6.2, 'Email Server\n(Invoices)', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
    ax.text(2, 5.0, 'File System\n(PDF/Excel)', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

    # Processing Layer (RPA + AI)
    ax.text(8, 7.5, 'Processing Core', fontsize=12, fontweight='bold', ha='center')
    ax.add_patch(patches.Rectangle((4, 2), 8, 5, facecolor='#e1f5fe', edgecolor='#0277bd', alpha=0.3))
    
    # RPA Bots
    ax.text(6, 6, 'RPA Orchestrator\n(Scheduler & Retry)', ha='center', va='center', bbox=dict(facecolor='#b1ddf0', edgecolor='#0277bd'))
    ax.text(6, 4.5, 'RPA Bots\n(UiPath / AA)', ha='center', va='center', bbox=component_style)
    
    # AI Services
    ax.text(10, 4.5, 'AI Services\n(FastAPI / Docker)', ha='center', va='center', bbox=ai_style)
    ax.text(10, 3.5, 'OCR & Classification\n(Tesseract/Sklearn)', ha='center', va='center', fontsize=8, bbox=dict(facecolor='white', edgecolor='green'))
    
    # Data & Monitoring Layer
    ax.text(14, 7.5, 'Data & Output', fontsize=12, fontweight='bold', ha='center')
    ax.add_patch(patches.Rectangle((12.5, 2), 3, 5, facecolor='#fff2cc', edgecolor='#d6b656', alpha=0.3))
    
    ax.text(14, 6, 'ERP System\n(SAP/Oracle)', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='orange'))
    ax.text(14, 4.5, 'Database\n(Logs/Analytics)', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='orange'))
    ax.text(14, 3, 'Dashboards\n(PowerBI/Python)', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='orange'))

    # Arrows
    def draw_arrow(x1, y1, x2, y2, label=""):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', lw=2, color='#555555'))
        if label:
            ax.text((x1+x2)/2, (y1+y2)/2 + 0.1, label, ha='center', fontsize=8)

    # Input -> RPA
    draw_arrow(3.5, 6, 4.8, 6) # Email -> Orchestrator
    draw_arrow(3.5, 5, 4.8, 4.5) # File -> Bots
    
    # Orchestrator -> Bots
    draw_arrow(6, 5.5, 6, 4.9)
    
    # Bots <-> AI
    draw_arrow(7.2, 4.5, 8.8, 4.5, "Rest API")
    draw_arrow(8.8, 4.3, 7.2, 4.3)
    
    # Bots -> ERP
    draw_arrow(7.2, 4.5, 12.8, 6, "Data Entry")
    
    # Bots -> DB
    draw_arrow(7.2, 4.5, 12.8, 4.5, "Logs")
    
    # DB -> Dashboard
    draw_arrow(14, 4.1, 14, 3.4)

    plt.tight_layout()
    plt.savefig('outputs/rpa_workflow_diagram.png', dpi=300)
    plt.close()
    print("Architecture diagram saved to outputs/rpa_workflow_diagram.png")

if __name__ == "__main__":
    create_architecture_diagram()
