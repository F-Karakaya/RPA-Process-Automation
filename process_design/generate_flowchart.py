import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_bpmn_diagram():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Styles
    box_style = dict(facecolor='#E6F3FF', edgecolor='#0066CC', boxstyle='round,pad=0.5')
    decision_style = dict(facecolor='#FFF2CC', edgecolor='#D6B656', boxstyle='darrow,pad=0.3')
    start_style = dict(facecolor='#D5E8D4', edgecolor='#82B366', boxstyle='circle,pad=0.5')
    end_style = dict(facecolor='#F8CECC', edgecolor='#B85450', boxstyle='circle,pad=0.5')
    
    # Nodes
    # Using text with bbox to simulate nodes
    ax.text(1, 7, 'Start\nEmail Received', ha='center', va='center', bbox=start_style, fontsize=10)
    
    ax.text(3.5, 7, 'RPA Bot\nDownloads Attachment', ha='center', va='center', bbox=box_style, fontsize=10)
    
    ax.text(6.5, 7, 'AI Service\nOCR & Classification', ha='center', va='center', bbox=box_style, fontsize=10)
    
    ax.text(9.5, 7, 'Confidence\n> 85%?', ha='center', va='center', bbox=decision_style, fontsize=10)
    
    # Path: High Confidence
    ax.text(12, 5, 'RPA Bot\nExtract Data', ha='center', va='center', bbox=box_style, fontsize=10)
    
    ax.text(12, 3, 'RPA Bot\nValidate w/ ERP', ha='center', va='center', bbox=box_style, fontsize=10)
    
    ax.text(9.5, 3, 'Validation\nSuccess?', ha='center', va='center', bbox=decision_style, fontsize=10)
    
    ax.text(6.5, 3, 'RPA Bot\nEnter Data in ERP', ha='center', va='center', bbox=box_style, fontsize=10)
    
    ax.text(3.5, 3, 'End\nProcess Complete', ha='center', va='center', bbox=end_style, fontsize=10)

    # Path: Low Confidence / Exceptions
    ax.text(9.5, 5, 'Human in Loop\nReview', ha='center', va='center', bbox=dict(facecolor='#FFE6CC', edgecolor='#D79B00', boxstyle='round,pad=0.5'), fontsize=10)
    
    # Arrows
    # Helper to draw arrows
    def draw_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color='#333333'))

    # Connections
    draw_arrow(1.5, 7, 2.2, 7) # Start -> Download
    draw_arrow(4.8, 7, 5.2, 7) # Download -> AI
    draw_arrow(7.8, 7, 8.5, 7) # AI -> Decision
    
    draw_arrow(10.5, 7, 10.8, 5.2) # Decision -> Extract (approx path for YES)
    ax.text(11, 6.5, 'Yes', fontsize=9, color='green')
    
    draw_arrow(9.5, 6.4, 9.5, 5.6) # Decision -> Human (NO)
    ax.text(9.6, 6, 'No', fontsize=9, color='red')
    
    draw_arrow(9.5, 4.4, 10.8, 5) # Human -> Extract (Manual fix loops back or proceeds) - simplify to Extract
    # Actually let's point Human to Extract or just merge.
    # Let's say Human validates and then we go to Extract/Verify.
    draw_arrow(9.5, 4.4, 11, 3.5) # Human -> Validate
    
    draw_arrow(12, 4.4, 12, 3.6) # Extract -> Validate
    
    draw_arrow(10.7, 3, 10.3, 3) # Validate -> Decision
    
    draw_arrow(8.7, 3, 7.8, 3) # Decision (Yes) -> Enter
    ax.text(8.2, 3.2, 'Yes', fontsize=9, color='green')
    
    draw_arrow(9.5, 2.4, 9.5, 4.4) # Decision (No) -> Human (Loop back)
    ax.text(9.6, 2.7, 'No', fontsize=9, color='red')
    
    draw_arrow(5.2, 3, 4.1, 3) # Enter -> End

    # Title
    ax.text(7, 0.5, 'RPA & AI Integrated Invoice Process Flow', ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.savefig('process_design/process_flow.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    create_bpmn_diagram()
