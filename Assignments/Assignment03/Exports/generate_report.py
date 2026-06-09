from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, black, grey
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib import colors
import os

BASE = r"C:\IaaC\AIA\GraphML\Assignments\Assignment03\Exports"
OUTPUT = os.path.join(BASE, "Zaro_Lakzhmy_Assignment03_BGR.pdf")

HEADER_LEFT = "Homework 03 — Building Graph Representation"
HEADER_RIGHT = "Zaro, Lakzhmy"

def header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    # Header line
    canvas.setStrokeColor(HexColor("#4a4a4a"))
    canvas.setLineWidth(0.5)
    canvas.line(50, h - 50, w - 50, h - 50)
    # Header text
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(HexColor("#4a4a4a"))
    canvas.drawString(50, h - 45, HEADER_LEFT)
    canvas.drawRightString(w - 50, h - 45, HEADER_RIGHT)
    # Page number
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(grey)
    canvas.drawCentredString(w / 2, 30, f"Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    topMargin=70,
    bottomMargin=60,
    leftMargin=50,
    rightMargin=50,
)

styles = getSampleStyleSheet()

style_title = ParagraphStyle("Title2", parent=styles["Title"], fontSize=22, spaceAfter=6,
                              textColor=HexColor("#333333"), fontName="Helvetica-Bold")
style_subtitle = ParagraphStyle("Subtitle2", parent=styles["Normal"], fontSize=13,
                                 alignment=TA_CENTER, spaceAfter=4, textColor=HexColor("#555555"))
style_subtitle_italic = ParagraphStyle("SubtitleItalic", parent=style_subtitle,
                                        fontName="Helvetica-Oblique", fontSize=11, spaceAfter=20)
style_h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=16, spaceBefore=20,
                           spaceAfter=10, textColor=HexColor("#333333"), fontName="Helvetica-Bold")
style_h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=13, spaceBefore=14,
                           spaceAfter=8, textColor=HexColor("#333333"), fontName="Helvetica-Bold")
style_body = ParagraphStyle("Body2", parent=styles["Normal"], fontSize=10, leading=14,
                             alignment=TA_JUSTIFY, spaceAfter=8)
style_caption = ParagraphStyle("Caption", parent=styles["Normal"], fontSize=9,
                                alignment=TA_CENTER, textColor=HexColor("#666666"),
                                fontName="Helvetica-Oblique", spaceBefore=4, spaceAfter=16)
style_code = ParagraphStyle("Code", parent=styles["Normal"], fontSize=9, fontName="Courier",
                             leading=13, spaceAfter=6, leftIndent=30)
style_bullet = ParagraphStyle("Bullet", parent=style_body, leftIndent=20, bulletIndent=10,
                               spaceBefore=2, spaceAfter=2)

story = []

# ---- TITLE ----
story.append(Spacer(1, 30))
story.append(Paragraph("<b>Homework 03</b>", style_title))
story.append(Paragraph("Building Graph Representation", style_subtitle))
story.append(Paragraph("<i>Graph Machine Learning — Session 06 (13A &amp; 13B)</i>", style_subtitle_italic))
story.append(HRFlowable(width="80%", thickness=1, color=HexColor("#aaaaaa"), spaceAfter=14, spaceBefore=6))

# Figure on title page - geometry overview
img_path = os.path.join(BASE, "geometry1.png")
if os.path.exists(img_path):
    story.append(Image(img_path, width=280, height=210, kind='proportional'))
    story.append(Paragraph("<i>Building overview — CellComplex coloured by spatial type</i>", style_caption))

# ---- THE BUILDING MODEL ----
story.append(Paragraph("The Building Model", style_h1))
story.append(Paragraph(
    "The building was modelled in Rhinoceros 3D and exported as four separate OBJ files, one for "
    "each spatial category: ground slab, structural columns, office volumes, and service core. Each "
    "file corresponds to a distinct node type in the graph and is loaded independently in the notebook.",
    style_body
))

# ---- PART 1 ----
story.append(Paragraph("Part 1 — Constructing the Graph (13A)", style_h1))

story.append(Paragraph("Loading and Tagging Geometry", style_h2))
story.append(Paragraph(
    "Each OBJ file was imported using <font name='Courier' size='9'>Topology.ByOBJPath</font> with "
    "<font name='Courier' size='9'>transposeAxes=True</font> to convert from OBJ's Y-up convention "
    "to Rhino's Z-up coordinate system. The imported faces were consolidated into closed volumetric "
    "cells via <font name='Courier' size='9'>Topology.SelfMerge</font>. A semantic tag — ground, "
    "column, office, or core — was then attached to each cell along with a display colour, stored as "
    "a dictionary on a selector point placed inside the volume.",
    style_body
))

story.append(Paragraph("Assembling the CellComplex", style_h2))
story.append(Paragraph(
    "All tagged cells were merged into a single CellComplex. Wherever two spaces share a wall, "
    "that surface becomes an internal face that encodes the adjacency — each cell implicitly knows "
    "its spatial neighbours through shared boundaries.",
    style_body
))

# Figure 1
img_path = os.path.join(BASE, "Import_Geometry.png")
if os.path.exists(img_path):
    story.append(Spacer(1, 6))
    story.append(Image(img_path, width=300, height=210, kind='proportional'))
    story.append(Paragraph("<i>Figure 1. CellComplex — merged volumetric model</i>", style_caption))

# Figure 2
img_path = os.path.join(BASE, "Color_Geometry.png")
if os.path.exists(img_path):
    story.append(Image(img_path, width=300, height=210, kind='proportional'))
    story.append(Paragraph("<i>Figure 2. CellComplex with type-based colouring (ground, columns, offices, core)</i>", style_caption))

story.append(Paragraph("Propagating Labels", style_h2))
story.append(Paragraph(
    "The selector dictionaries were transferred onto the unified cells using "
    "<font name='Courier' size='9'>Topology.TransferDictionariesBySelectors</font>, ensuring that "
    "every cell in the CellComplex retains its type label after the merge operation.",
    style_body
))

story.append(Paragraph("Converting to a Graph", style_h2))
story.append(Paragraph(
    "<font name='Courier' size='9'>Graph.ByTopology</font> converted the CellComplex into an "
    "attributed graph: each cell becomes a node and each shared internal face becomes an edge. "
    "Node types were one-hot encoded as five-dimensional feature vectors:",
    style_body
))

story.append(Paragraph("ground  &rarr;  [1, 0, 0, 0, 0]", style_code))
story.append(Paragraph("column  &rarr;  [0, 1, 0, 0, 0]", style_code))
story.append(Paragraph("office  &rarr;  [0, 0, 0, 1, 0]", style_code))
story.append(Paragraph("core    &rarr;  [0, 0, 0, 0, 1]", style_code))

story.append(Paragraph(
    "The plinth category (index 2) was not used in this building. The feature matrix was exported "
    "to CSV as <font name='Courier' size='9'>feature_00</font> through "
    "<font name='Courier' size='9'>feature_04</font>, alongside node coordinates, edge lists, "
    "and the manually assigned graph label.",
    style_body
))

# ---- PART 2 ----
story.append(Paragraph("Part 2 — Predicting the Label (13B)", style_h1))

story.append(Paragraph("Training the Model", style_h2))
story.append(Paragraph(
    "A GNN classifier was trained on the instructor-provided dataset "
    "(<font name='Courier' size='9'>dataset_graph_classification</font>) using PyTorch Geometric. "
    "The model performs graph-level classification into one of five building-ground relationship categories:",
    style_body
))

categories = [
    ("0 — Separation", "the building is raised on pilotis with no direct ground contact"),
    ("1 — Separation with Plinth", "raised volume, but a solid base mediates the transition"),
    ("2 — Adherence", "floor planes sit flush on the ground without an intermediary"),
    ("3 — Adherence with Plinth", "grounded, but a podium extends and anchors the footprint"),
    ("4 — Interlock", "the ground plane penetrates into the building volume, blurring the boundary"),
]
for cat, desc in categories:
    story.append(Paragraph(f"<bullet>&bull;</bullet><b>{cat}</b> — {desc}", style_bullet))

story.append(Spacer(1, 8))

# Figure 4 - Training curves
img_path = os.path.join(BASE, "Training_Validation_Loss_Curves_plot.png")
if os.path.exists(img_path):
    story.append(Image(img_path, width=420, height=160, kind='proportional'))
    story.append(Paragraph("<i>Figure 4. Training and Validation Loss Curves</i>", style_caption))

story.append(Paragraph("Prediction", style_h2))
story.append(Paragraph(
    "The exported CSV dataset was loaded into a PyTorch Geometric data object and passed to the "
    "pre-trained model <font name='Courier' size='9'>bgr_model.pt</font> via the "
    "<font name='Courier' size='9'>Predict()</font> function. The output table compares the manually "
    "assigned label against the model's prediction and reports a confidence score.",
    style_body
))

# Prediction results table
table_data = [
    ["Actual\nValue", "Predicted\nValue", "Actual Label", "Predicted\nLabel", "Confidence"],
    ["0", "1", "Separation", "Separation\nwith Plinth", "1.0"],
]

t = Table(table_data, colWidths=[70, 70, 90, 90, 70])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor("#4a4a4a")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
    ('BACKGROUND', (0, 1), (-1, -1), HexColor("#f5f5f5")),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))
story.append(t)
story.append(Paragraph("<i>Table 1. Prediction results from bgr_model.pt</i>", style_caption))

# Figure 5 - Confusion matrix
img_path = os.path.join(BASE, "Confusion_Matrix.png")
if os.path.exists(img_path):
    story.append(Image(img_path, width=280, height=210, kind='proportional'))
    story.append(Paragraph("<i>Figure 5. Confusion Matrix</i>", style_caption))

# ---- REFLECTION ----
story.append(Paragraph("Reflection — Separation vs. Separation with Plinth", style_h1))

story.append(Paragraph(
    "The manually assigned label was 0 (Separation), while the model predicted 1 "
    "(Separation with Plinth) with a confidence of 1.0. The discrepancy is meaningful and worth examining.",
    style_body
))

story.append(Paragraph(
    "The building features a ground slab with columns lifting portions of the structure above it. "
    "The core has a single geometry whose base sits flush to the ground. The columns also sit flush "
    "on the ground slab. For the offices, only some first-level volumes rest on columns, while the "
    "upper levels stack on top of each other. Based on this reading — volumes touching the ground "
    "face-to-face but not overlapping — the assigned label of Separation seemed appropriate.",
    style_body
))

story.append(Paragraph(
    "However, the GNN classified the graph as Separation with Plinth with full confidence. The model "
    "likely interprets the ground slab as a plinth — a continuous platform that mediates between the "
    "earth and the building above. From a topological perspective, the ground slab is a highly connected "
    "node adjacent to columns, core, and some office cells. This connectivity pattern resembles a plinth "
    "more than a simple separation layer, because the ground node acts as a shared base that multiple "
    "spatial types connect through rather than a passive surface beneath isolated pilotis.",
    style_body
))

story.append(Paragraph(
    "This highlights a key insight about graph-based classification: the model reads spatial relationships "
    "through topology (adjacency), not geometry (shape, height, thickness). A thin ground slab and a thick "
    "plinth may produce identical graph structures, making them indistinguishable to the GNN. Richer node "
    "features — such as volume, height, or surface area — could help the model differentiate these cases.",
    style_body
))

# Build
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(f"PDF created: {OUTPUT}")
