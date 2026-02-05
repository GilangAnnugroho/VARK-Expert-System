import plotly.graph_objects as go
from collections import Counter
from modules.data import STRATEGIES

class InferenceEngine:
    def __init__(self):
        self.scores = {"V": 0, "A": 0, "R": 0, "K": 0}

    def process_answers(self, answers):
        self.scores = {"V": 0, "A": 0, "R": 0, "K": 0}
        counts = Counter(answers)
        for key in self.scores:
            self.scores[key] = counts.get(key, 0)
        return self.scores

    def calculate_percentages(self):
        total = sum(self.scores.values())
        if total == 0: return {k: 0 for k in self.scores}
        return {k: round((v / total) * 100) for k, v in self.scores.items()}

    def determine_profile(self):
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
        top_1_code, top_1_val = sorted_scores[0]
        top_2_code, top_2_val = sorted_scores[1]
        
        if (top_1_val - top_2_val) < 2 and top_2_val > 0:
            return "Multimodal", STRATEGIES["Multimodal"]
        else:
            return top_1_code, STRATEGIES[top_1_code]

    def create_radar_chart(self):
        """
        Membuat Chart Radar Modern yang bersih dan sesuai tema UI.
        """
        categories = [
            f"Visual ({self.scores['V']})", 
            f"Aural ({self.scores['A']})", 
            f"Read/Write ({self.scores['R']})", 
            f"Kinesthetic ({self.scores['K']})"
        ]
        values = [self.scores['V'], self.scores['A'], self.scores['R'], self.scores['K']]
        categories = [*categories, categories[0]]
        values = [*values, values[0]]
        fig = go.Figure(data=[go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Skor',
            line_color='#6366f1',
            fillcolor='rgba(99, 102, 241, 0.2)',
            mode='lines+markers',
            marker=dict(size=6, color='#4f46e5', symbol='circle'),
        )])

        max_val = max(values) if max(values) > 0 else 5
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max_val + 1],
                    gridcolor='rgba(0,0,0,0.06)', 
                    linecolor='rgba(0,0,0,0)',   
                    tickfont=dict(size=9, color='#94a3b8'), 
                    showline=False,
                    tickangle=0
                ),
                angularaxis=dict(
                    tickfont=dict(size=11, color='#334155', family="Poppins", weight="bold"),
                    rotation=90,
                    direction="clockwise",
                    gridcolor='rgba(0,0,0,0.06)'
                ),
                bgcolor='rgba(255,255,255,0)' 
            ),
            showlegend=False,
            margin=dict(l=50, r=50, t=30, b=30),
            height=300, 
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Poppins")
        )
        return fig