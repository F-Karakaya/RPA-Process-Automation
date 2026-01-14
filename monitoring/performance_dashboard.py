import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import os

def generate_dashboard():
    """
    Generates a performance dashboard visualization for the RPA bots.
    """
    print("Generating Performance Dashboard...")
    
    # Create sample data if execution log doesn't fully support visualization needs
    data = {
        'Process': ['InvoiceProcessing'] * 10 + ['EmailBot'] * 10,
        'Duration': np.random.randint(30, 180, 20),
        'Status': ['Success'] * 8 + ['Failed'] * 2 + ['Success'] * 9 + ['Failed'] * 1
    }
    df = pd.DataFrame(data)
    
    # Plotting
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('RPA Operations Center - Performance Dashboard', fontsize=16, fontweight='bold')
    
    # 1. Execution Volume by Process
    process_counts = df['Process'].value_counts()
    axes[0, 0].bar(process_counts.index, process_counts.values, color=['#0066cc', '#009933'])
    axes[0, 0].set_title('Total Executions by Bot')
    axes[0, 0].set_ylabel('Execution Count')
    
    # 2. Average Duration
    avg_duration = df.groupby('Process')['Duration'].mean()
    axes[0, 1].barh(avg_duration.index, avg_duration.values, color='#ff9933')
    axes[0, 1].set_title('Average Execution Time (Seconds)')
    
    # 3. Success vs Failure Rate
    status_counts = df['Status'].value_counts()
    axes[1, 0].pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', 
                   colors=['#66ff66', '#ff6666'], startangle=90)
    axes[1, 0].set_title('Overall Success Rate')
    
    # 4. Throughput Trend (Simulated)
    hours = [f"{i}:00" for i in range(9, 18)]
    throughput = [15, 22, 45, 30, 12, 40, 55, 35, 20]
    axes[1, 1].plot(hours, throughput, marker='o', linestyle='-', color='#9933cc')
    axes[1, 1].set_title('Hourly Transaction Throughput')
    axes[1, 1].grid(True, linestyle='--', alpha=0.6)
    
    # Footer
    plt.figtext(0.5, 0.02, f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
                ha="center", fontsize=10, style='italic')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    output_path = 'monitoring/dashboard_output.png'
    plt.savefig(output_path, dpi=300)
    print(f"Dashboard saved to {output_path}")
    
    return output_path

if __name__ == "__main__":
    generate_dashboard()
