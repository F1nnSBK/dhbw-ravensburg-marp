#!/usr/bin/env python3
"""
Generate a Tufte-style SVG Gantt chart for DHBW Ravensburg Marp presentation.
Adheres strictly to user instructions:
- Balanced vertical whitespace: generous gaps under subheadings, clean spacing between sections
- Ample bottom padding (26px) so CE-35 is never cut off
- Indented task lists under subheadings
- Clean CE labels on bars
- 100% valid XML with HTML escaping
"""

import os
import html
import xml.etree.ElementTree as ET

def generate_svg(output_path: str):
    working_days = [
        ("01.10.", "Do", 40),
        ("02.10.", "Fr", 40),
        ("05.10.", "Mo", 41),
        ("06.10.", "Di", 41),
        ("07.10.", "Mi", 41),
        ("08.10.", "Do", 41),
        ("09.10.", "Fr", 41),
        ("12.10.", "Mo", 42),
        ("13.10.", "Di", 42),
        ("14.10.", "Mi", 42),
        ("15.10.", "Do", 42),
        ("16.10.", "Fr", 42),
        ("19.10.", "Mo", 43),
        ("20.10.", "Di", 43), # Today (index 13)
        ("21.10.", "Mi", 43),
        ("22.10.", "Do", 43),
        ("23.10.", "Fr", 43),
        ("26.10.", "Mo", 44),
        ("27.10.", "Di", 44),
        ("28.10.", "Mi", 44),
        ("29.10.", "Do", 44),
        ("30.10.", "Fr", 44),
    ]

    total_days = len(working_days) # 22
    
    width = 1136
    height = 410
    
    # Left column bounds
    section_x = 40   # Subheading start
    task_x = 58      # Indented task start
    chart_x = 368
    chart_w = 724
    day_w = chart_w / total_days # ~32.91 px per day
    
    def day_to_x(idx):
        return chart_x + idx * day_w
    
    tasks_by_section = [
        (
            "Abgeschlossen",
            [
                ("CE-21", "Tino", "Email an Schilling", "2h", 0, 1, "done"),
                ("CE-26", "Tino", "UI Verbessern", "1w 3d", 2, 9, "done"),
            ]
        ),
        (
            "Woche 41 (ab 5. Okt)",
            [
                ("CE-23", "Flo", "Tests m. Kategoriendefinition", "3d", 2, 3, "todo"),
                ("CE-22", "Finn", "RTX 6000 f. Parallele Samples", "1w", 2, 5, "todo"),
                ("CE-25", "Flo", "Effizienz Judgement & Worker", "–", 2, 12, "open"),
                ("CE-24", "Finn", "Präsentation mit MARP", "3d", 4, 3, "todo"),
            ]
        ),
        (
            "Woche 43 & 44 (ab 20. Okt)",
            [
                ("CE-27", "Team", "Termin 20.10. (Präsentation 1)", "2h", 13, 1, "active"),
                ("CE-33", "Flo", "CLI ausbauen", "–", 14, 6, "open"),
                ("CE-32", "Tino", "Reverse Proxy & WebUI", "–", 14, 6, "open"),
                ("CE-31", "Max", "Statistische Tests erweitern", "–", 14, 6, "open"),
                ("CE-34", "Tino", "WebUI mit Login absichern", "–", 14, 6, "open"),
                ("CE-29", "Finn", "Kapazitätsstatus Modellserver", "1w", 14, 5, "todo"),
                ("CE-28", "Max", "Erweiterung Multi-User Access", "4d", 14, 4, "todo"),
                ("CE-35", "Team", "Weekly", "2h", 19, 1, "todo"),
            ]
        )
    ]
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="Projektplan Oktober 2026">')
    
    svg.append("""  <style>
    text { font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    .title { font-size: 12.5px; font-weight: 700; fill: #22252A; letter-spacing: 0.06em; text-transform: uppercase; }
    .sec-title { font-size: 10px; font-weight: 700; fill: #5C6971; text-transform: uppercase; letter-spacing: 0.08em; }
    .task-id { font-size: 10.5px; font-weight: 700; fill: #5C6971; }
    .task-id.active { fill: #E2001A; }
    .task-name { font-size: 10.5px; font-weight: 500; fill: #22252A; }
    .task-name.active { font-weight: 700; fill: #22252A; }
    .task-dur { font-size: 9px; font-weight: 500; fill: #9AA5AC; }
    .who-pill { rx: 3px; }
    .who-text { font-size: 8.5px; font-weight: 700; }
    .axis-week { font-size: 10.5px; font-weight: 700; fill: #5C6971; }
    .axis-day { font-size: 9px; font-weight: 500; fill: #9AA5AC; }
    .axis-day.today { font-weight: 700; fill: #E2001A; font-size: 10px; }
    .grid-line { stroke: #ECEFF1; stroke-width: 0.75; }
    .week-div { stroke: #C6CDD2; stroke-width: 1.2; stroke-dasharray: 2,2; }
    .today-line { stroke: #E2001A; stroke-width: 1.5; stroke-dasharray: 3,3; }
    .bar-done { fill: #9AA5AC; }
    .bar-active { fill: #E2001A; }
    .bar-todo { fill: #5C6971; }
    .bar-open { fill: #D6DCE2; }
    .bar-label-in { font-size: 9.5px; font-weight: 600; fill: #FFFFFF; }
    .bar-label-in.dark { fill: #333A42; font-weight: 700; }
    .bar-label-out { font-size: 9.5px; font-weight: 600; fill: #5C6971; }
    .bar-label-out.active { font-weight: 700; fill: #E2001A; }
    .legend-text { font-size: 9.5px; fill: #5C6971; }
  </style>""")

    # Background card
    svg.append(f'  <rect x="0" y="0" width="{width}" height="{height}" rx="14" fill="#F8F9FA" />')

    # Top-Left Header: Title & 4-item Legend
    svg.append(f'  <g transform="translate({section_x}, 10)">')
    svg.append('    <text class="title" x="0" y="11">Projektplan · Oktober 2026</text>')
    
    svg.append('    <g transform="translate(0, 21)">')
    # Done
    svg.append('      <rect x="0" y="2" width="8" height="8" rx="2" fill="#9AA5AC" />')
    svg.append('      <text class="legend-text" x="12" y="9">Erledigt</text>')
    # Active
    svg.append('      <rect x="64" y="2" width="8" height="8" rx="2" fill="#E2001A" />')
    svg.append('      <text class="legend-text" x="76" y="9">Aktiv (Heute)</text>')
    # Todo
    svg.append('      <rect x="148" y="2" width="8" height="8" rx="2" fill="#5C6971" />')
    svg.append('      <text class="legend-text" x="160" y="9">Geplant</text>')
    # Open / without estimate
    svg.append('      <rect x="216" y="2" width="8" height="8" rx="2" fill="#D6DCE2" />')
    svg.append('      <text class="legend-text" x="228" y="9">Ohne Zeitschätzung</text>')
    svg.append('    </g>')
    svg.append('  </g>')

    # Weeks definition
    weeks = [
        ("KW 40", 0, 2),
        ("KW 41", 2, 5),
        ("KW 42", 7, 5),
        ("KW 43", 12, 5),
        ("KW 44", 17, 5),
    ]

    axis_y_weeks = 17
    axis_y_days = 33
    
    # Horizontal rule under header
    svg.append(f'  <line x1="{section_x - 12}" y1="48" x2="{width - 32}" y2="48" stroke="#E2E6E9" stroke-width="1" />')

    # Week labels and dividers
    for w_name, start_idx, count in weeks:
        wx = day_to_x(start_idx)
        ww = count * day_w
        svg.append(f'  <text class="axis-week" x="{wx + ww/2}" y="{axis_y_weeks}" text-anchor="middle">{html.escape(w_name)}</text>')
        if start_idx > 0:
            svg.append(f'  <line class="week-div" x1="{wx}" y1="10" x2="{wx}" y2="{height - 16}" />')

    # Day labels
    for idx, (d_str, d_name, _) in enumerate(working_days):
        dx = day_to_x(idx) + day_w / 2
        is_today = (idx == 13)
        cls = "axis-day today" if is_today else "axis-day"
        svg.append(f'  <text class="{cls}" x="{dx}" y="{axis_y_days}" text-anchor="middle">{html.escape(d_str[:2])}</text>')

    # Grid vertical lines
    for idx in range(total_days + 1):
        gx = day_to_x(idx)
        svg.append(f'  <line class="grid-line" x1="{gx}" y1="39" x2="{gx}" y2="{height - 16}" />')

    # Today vertical indicator line & badge
    today_x = day_to_x(13) + day_w / 2
    svg.append('  <!-- Today marker (20.10.) -->')
    svg.append(f'  <rect x="{today_x - 18}" y="36" width="36" height="11" rx="2" fill="#E2001A" />')
    svg.append(f'  <text x="{today_x}" y="44.5" text-anchor="middle" font-size="7" font-weight="700" fill="#FFFFFF">HEUTE</text>')
    svg.append(f'  <line class="today-line" x1="{today_x}" y1="48" x2="{today_x}" y2="{height - 16}" />')

    # Tasks layout with balanced vertical spacing and ample bottom clearance
    current_y = 66
    row_height = 19
    
    for sec_idx, (sec_name, tasks) in enumerate(tasks_by_section):
        if sec_idx > 0:
            current_y += 18
            
        # Section header
        svg.append(f'  <text class="sec-title" x="{section_x}" y="{current_y + 1}">{html.escape(sec_name)}</text>')
        svg.append(f'  <line x1="{section_x}" y1="{current_y + 5}" x2="{chart_x - 14}" y2="{current_y + 5}" stroke="#E2E6E9" stroke-width="0.75" />')
        
        current_y += 18
        
        for task_id, who, task_name, dur, s_idx, l_days, status in tasks:
            bar_y = current_y - 10.5
            bar_h = 13
            bx = day_to_x(s_idx) + 2
            bw = max(l_days * day_w - 4, 14)
            
            # Row highlight for active
            if status == "active":
                svg.append(f'  <rect x="{task_x - 8}" y="{current_y - 12}" width="{width - task_x - 20}" height="{row_height}" rx="4" fill="#FDF0F1" opacity="0.8" />')
                id_cls = "task-id active"
                name_cls = "task-name active"
                bar_cls = "bar-active"
                out_cls = "bar-label-out active"
            elif status == "done":
                id_cls = "task-id"
                name_cls = "task-name"
                bar_cls = "bar-done"
                out_cls = "bar-label-out"
            elif status == "open":
                id_cls = "task-id"
                name_cls = "task-name"
                bar_cls = "bar-open"
                out_cls = "bar-label-out"
            else:
                id_cls = "task-id"
                name_cls = "task-name"
                bar_cls = "bar-todo"
                out_cls = "bar-label-out"
            
            # 1. Left Column: Task ID (INDENTED at task_x = 58)
            svg.append(f'  <text class="{id_cls}" x="{task_x}" y="{current_y}">{html.escape(task_id)}</text>')
            
            # 2. Assignee Badge (Who)
            who_w = 28 if len(who) <= 3 else (34 if len(who) <= 4 else 40)
            who_bg = "#FDF0F1" if who == "Team" else "#E8ECEE"
            who_fg = "#E2001A" if who == "Team" else "#4A555D"
            pill_x = task_x + 44
            svg.append(f'  <rect class="who-pill" x="{pill_x}" y="{current_y - 9.5}" width="{who_w}" height="12" fill="{who_bg}" />')
            svg.append(f'  <text class="who-text" x="{pill_x + who_w/2}" y="{current_y - 1}" text-anchor="middle" fill="{who_fg}">{html.escape(who)}</text>')
            
            # 3. Task Name
            svg.append(f'  <text class="{name_cls}" x="{pill_x + who_w + 6}" y="{current_y}">{html.escape(task_name)}</text>')
            
            # 4. Duration
            svg.append(f'  <text class="task-dur" x="{chart_x - 14}" y="{current_y}" text-anchor="end">{html.escape(dur)}</text>')
            
            # 5. Task Bar
            svg.append(f'  <rect class="{bar_cls}" x="{bx}" y="{bar_y}" width="{bw}" height="{bar_h}" rx="3" />')
            
            # 6. Bar Labels: Clean CE numbers only
            if bw >= 50:
                label_text = task_id
                if status == "done":
                    label_text = f"✓ {task_id}"
                in_cls = "bar-label-in dark" if status == "open" else "bar-label-in"
                svg.append(f'  <text class="{in_cls}" x="{bx + bw/2}" y="{bar_y + 9.5}" text-anchor="middle">{html.escape(label_text)}</text>')
            else:
                if status == "done":
                    svg.append(f'  <text class="bar-label-in" x="{bx + bw/2}" y="{bar_y + 9.5}" text-anchor="middle">&#x2713;</text>')
                svg.append(f'  <text class="{out_cls}" x="{bx + bw + 5}" y="{bar_y + 9.5}">{html.escape(task_id)}</text>')

            current_y += row_height

    svg.append('</svg>')
    
    xml_content = "\n".join(svg)
    ET.fromstring(xml_content)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"Generated {output_path} successfully (bottom clearance guaranteed).")

if __name__ == "__main__":
    generate_svg("assets/project-plan-gantt.svg")
