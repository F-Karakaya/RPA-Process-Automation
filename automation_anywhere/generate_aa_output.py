import matplotlib.pyplot as plt

def create_aa_dashboard():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('#f0f0f0')
    
    # Simulate a Bot Runner Status Window
    ax.text(0.5, 0.9, 'Automation Anywhere Enterprise Client', 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#FF6600')
            
    ax.text(0.1, 0.8, 'Bot Performance', fontsize=12, fontweight='bold')
    
    # Draw a table or status list
    data = [
        ['Bot Name', 'Status', 'Last Run', 'Success'],
        ['Email Ticket Bot', 'Running...', 'Now', '98%'],
        ['Invoice Processor', 'Completed', '10:00 AM', '99%'],
        ['HR Onboarding', 'Scheduled', '12:00 PM', '100%']
    ]
    
    table = ax.table(cellText=data, loc='center', cellLoc='left', colWidths=[0.3, 0.2, 0.2, 0.2])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2)
    
    # Add a success message box at the bottom
    ax.text(0.5, 0.2, '✔ Email Ticket Bot: Successfully processed 15 new emails.', 
            ha='center', va='center', fontsize=12, color='green', 
            bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=1'))

    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('automation_anywhere/output_sample.png', dpi=100)
    plt.close()

if __name__ == "__main__":
    create_aa_dashboard()
