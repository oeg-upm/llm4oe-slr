
import plotly.graph_objects as go
import colorsys
import textwrap


original_labels = [
    "Requirements specification", "Ontology implementation", "Ontology publication", "Ontology maintenance",
    "Functional requirements writing", "CQ reverse engineering", "Requirement formalization",
    "Conceptualization", "Encoding", "Ontology matching", "Ontology evaluation",
    "Ontology documentation", "Bug issues"
]


original_parents = [
    "", "", "", "",
    "Requirements specification", "Requirements specification", "Requirements specification",
    "Ontology implementation", "Ontology implementation", "Ontology implementation", "Ontology implementation",
    "Ontology publication",
    "Ontology maintenance"
]


values = [
    18, 31, 5, 3.5,
    6, 8, 4,
    9, 9, 7, 6,
    5,
    3.5
]


true_values = {
    "Requirements specification": 10,
    "Ontology implementation": 25,
    "Ontology publication": 5,
    "Ontology maintenance": 1,
    "Functional requirements writing": 2,
    "CQ reverse engineering": 6,
    "Requirement formalization": 3,
    "Conceptualization": 10,
    "Encoding": 10,
    "Ontology matching": 5,
    "Ontology evaluation": 4,
    "Ontology documentation": 5,
    "Bug issues": 1
}


total = 41


phase_colors = {
    "Requirements specification": "#f6b26b",
    "Ontology implementation": "#9fc5e8",
    "Ontology publication": "#b6d7a8",
    "Ontology maintenance": "#b4a7d6"
}

custom_labels = {
    "Requirements specification": "Requirements specification",
    "Ontology implementation": "Ontology implementation",
    "Ontology publication": "Ontology<br>publication",
    "Ontology maintenance": "Ontology<br>maintenance",
    "Functional requirements writing": "Functional requirements<br>writing",
    "CQ reverse engineering": "CQ reverse<br>engineering",
    "Requirement formalization": "Requirement<br>formalization",
    "Conceptualization": "Conceptualization",
    "Encoding": "Encoding",
    "Ontology matching": "Ontology matching",
    "Ontology evaluation": "Ontology<br>evaluation",
    "Ontology documentation": "Ontology<br>documentation",
    "Bug issues": "Bug issues"
}


def lighten_color(hex_color, amount=0.5):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    l = min(1, l + amount * (1.0 - l))
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))


label_map = {}
reverse_label_map = {}
updated_labels = []


    # Replace the label processing section with this code:
for label in original_labels:
    true_value = true_values[label]
    percent = true_value / total * 100
    manual_label = custom_labels[label] 
    new_label = f"{manual_label}\n{true_value} ({percent:.1f}%)"
    
    updated_labels.append(new_label)
    label_map[label] = new_label  
    reverse_label_map[new_label] = label  


updated_parents = []
for parent in original_parents:
    if parent == "":
        updated_parents.append("")
    else:
        updated_parents.append(label_map[parent])

# color
colors = []
for label, parent in zip(updated_labels, updated_parents):
    if parent == "":
        original_label = reverse_label_map[label]
        colors.append(phase_colors[original_label])
    else:
        original_parent_label = reverse_label_map[parent]
        colors.append(lighten_color(phase_colors[original_parent_label], amount=0.5))


fig = go.Figure(go.Treemap(
    labels=updated_labels,
    parents=updated_parents,
    values=values,
    marker=dict(colors=colors, line=dict(color="black", width=0.8)),
    branchvalues="total",
    textinfo="label",
    textposition="middle center",
    insidetextfont=dict(size=48, color="black", family="Arial Black"), 
    hovertemplate='<b>%{label}</b><extra></extra>',
))

fig.update_layout(
    width=1400,   
    height=480,  
    uniformtext=dict(minsize=12, mode='hide'),
    margin=dict(t=40, l=25, r=25, b=25),
    font=dict(size=22, family="Arial Black")
)


fig.update_traces(
    marker=dict(colors=colors, line=dict(color="white", width=0.5)),
    insidetextfont=dict(size=38, color="black", family="Arial Black"),
    textposition="middle center"
)

fig.show()
