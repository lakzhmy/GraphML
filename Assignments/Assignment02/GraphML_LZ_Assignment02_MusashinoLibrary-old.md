# GraphML Assignment 2 — Lakzhmy
## Spatial Organization Report

### Overview

This report interprets the results of a graph-based analysis applied to the floor plan of the Musashino Art University Library (Sou Fujimoto Architects, 2010). The floor plan was converted into a spatial graph by overlaying a 1×1-unit grid, slicing it into discrete face cells, and deriving an analysis graph where each cell is a node and shared adjacencies are edges.

Three metrics were computed and visualized: the **Analysis Graph** (spatial network), **Closeness Centrality**, and **Shortest Path**.

The floor plan has two morphologically distinct zones: a dense, open lower reading area where the spiral bookshelf walls converge, and a branching upper zone where the same shelves fan outward into smaller, more enclosed bays. This contrast drives every metric computed.

---

## 1. Analysis Graph — Spatial Network

![Analysis Graph](Exports/Musashino_Show_AnalysisGraph.png)

![Analysis Graph (Navigation)](Exports/Musashino_Show_AnalysisGraph_2.png)

The analysis graph overlays the spatial network onto the floor plan. Each red dot is a node (face cell centroid) and each red line is a direct spatial connection between two adjacent cells.

**Key findings:**

- The **lower-central area** — the open reading and browsing zone between the converging shelf spirals — produces the densest node-edge cluster. Cells here have up to four neighbours in all directions, indicating a freely traversable, open floor.
- The **black voids** cutting through the graph correspond to the bookshelf walls and structural masses. These are physically inaccessible cells that fragment the graph locally and force movement to route around them.
- The **upper zone**, where the shelf-walls branch into a tree-like arrangement, shows significantly sparser connectivity. Node clusters are separated by voids, and several cells appear as near-terminal — reachable only through one or two adjacent cells. This is consistent with more enclosed, destination-type spaces (quiet reading bays, specialist collections).
- The **east perimeter** maintains a relatively continuous chain of connected cells running the full height of the building, suggesting it functions as a long-distance routing edge even without being a designated corridor.

---

## 2. Closeness Centrality

![Closeness Centrality](Exports/Musashino_Show_Heat.png)

Closeness centrality measures how quickly a space can reach all other spaces in the network. Bright yellow-orange indicates high global accessibility; dark blue-purple indicates spaces that are topologically remote.

**Key findings:**

- The **brightest region** — highest closeness — sits in the lower-central area of the floor plan, at the convergence point of the spiral bookshelf system. This is the building's topological centre of mass: a space with the shortest average path distance to every other cell in the graph.
- A **warm gradient** extends outward from this core, covering the open mid-floor zones in orange and amber. These intermediate areas are well-connected but require passing through the central zone to reach the far reaches of the building.
- The **upper branching zone** is consistently blue-purple, confirming that the shelf-wall bays are topologically deep. Reaching them from most other spaces requires many traversal steps — they are intentionally remote, suited to quiet or contemplative use.
- The **north corner** (the canopy/overhang area visible at the top) is the darkest region in the heatmap — the most peripheral space in the entire floor plan, with the highest topological depth.
- The **perimeter edges** (east and west) are uniformly low-closeness, consistent with boundary cells that connect on only one side. Despite their role in long-distance routing, they are not globally central.

Architecturally, this metric confirms that Fujimoto's spiral convergence is not only the spatial but also the topological heart of the building. The increasing depth toward the outer bays is a deliberate design move — the shelf-walls generate accessibility gradient as an experiential device, rewarding exploratory movement with progressively quieter spaces.

---

## 3. Shortest Path

![Shortest Path](Exports/Musashino_Show_ShortestPath.png)

The shortest path was computed from the upper-left corner to the lower-right corner of the floor plan — a full diagonal traversal of the building. Red shows the original topological path (114.46 units); blue shows the geometrically straightened version (109.37 units).

**Key findings:**

- Both the original and straightened paths **travel along the right (east) perimeter** of the building from top to bottom, rather than cutting through the interior. The bookshelf walls make any diagonal interior route topologically longer, so the perimeter becomes the efficient choice.
- The **4.4% savings** from straightening (5.09 units) is small, indicating the navigation graph already finds a geometrically efficient route — there is little redundancy in the topology of the perimeter edge.
- The **interior open zone**, despite having the highest closeness centrality, does not appear in the long-distance path because it supports local, diffuse browsing movement rather than directional traversal.
- This reveals a **dual circulation logic**: the high-centrality core handles local movement and browsing; the east perimeter handles fast, long-distance crossing. The building has two distinct movement modes operating simultaneously without interference.

---

## Summary: Spatial Organization

**Circulation Patterns**
The building operates with two overlapping circulation systems. Local movement is diffuse and exploratory, absorbed by the open central zone where high connectivity allows free-form browsing. Long-distance movement is channelled to the east perimeter — the building's only uninterrupted edge — since the bookshelf walls prevent efficient diagonal traversal through the interior.

**Hierarchy of Spaces**
There is a clear spatial hierarchy. At the top sits the open central convergence zone (highest closeness centrality), which acts as the building's spatial anchor. Below it are the transitional mid-floor areas — accessible but not primary. At the base are the deep shelf-wall bays in the upper branching zone, which are destination spaces with limited onward connectivity.

**Accessibility and Connectivity**
Accessibility is unevenly but intentionally distributed. The central core is maximally accessible; the outer bays are deliberately remote. The perimeter provides compensatory connectivity for long-distance movement, ensuring the building remains navigable even when the interior is obstructed. There is no single bottleneck node whose removal would sever the building — the graph is robust because the open floor area provides multiple parallel routing options.

**Functional Zoning**
The graph reveals three emergent zones without explicit walls: an **open-access core** (lower-centre, highest centrality) for primary browsing and reading; a **transitional branching zone** (mid-floor, intermediate centrality) where the shelf corridors channel movement between open and enclosed areas; and **deep destination bays** (upper zone, lowest closeness) suited to quiet or specialised use. This gradient — from public and diffuse to private and deep — is the spatial argument of the building, and the graph makes it legible numerically.

---

**Why graph analysis is useful for architectural datasets**
Graph analysis turns qualitative spatial intuition into measurable, comparable values. The closeness heatmap confirmed what the eye suspects — the spiral centre is the core — but it also revealed *how much deeper* the outer bays are, and exposed the perimeter's hidden routing role, which is invisible in a standard floor plan reading. For a building as geometrically complex as Musashino, where the walls are also the shelves and the circulation, graph analysis is the only tool that can separate structure from experience and make the logic of the plan explicit.
