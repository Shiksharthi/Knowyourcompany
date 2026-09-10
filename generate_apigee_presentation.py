"""
Generate PowerPoint Presentation for Apigee Multi-Region Configuration & 502 Debugging
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Define color scheme
    AUTOZONE_ORANGE = RGBColor(255, 102, 0)
    DARK_BLUE = RGBColor(0, 51, 102)
    LIGHT_GRAY = RGBColor(240, 240, 240)
    WHITE = RGBColor(255, 255, 255)

    # Slide 1: Title Slide
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout

    # Background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BLUE

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1))
    title_frame = title_box.text_frame
    title_frame.text = "Apigee Multi-Region Configuration"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(44)
    title_para.font.bold = True
    title_para.font.color.rgb = WHITE
    title_para.alignment = PP_ALIGN.CENTER

    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.5), Inches(9), Inches(0.8))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = "& 502 Error Debugging Guide"
    subtitle_para = subtitle_frame.paragraphs[0]
    subtitle_para.font.size = Pt(32)
    subtitle_para.font.color.rgb = AUTOZONE_ORANGE
    subtitle_para.alignment = PP_ALIGN.CENTER

    # Date and Author
    footer_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.5), Inches(9), Inches(0.5))
    footer_frame = footer_box.text_frame
    footer_frame.text = "Technical Program Manager | September 2026"
    footer_para = footer_frame.paragraphs[0]
    footer_para.font.size = Pt(16)
    footer_para.font.color.rgb = WHITE
    footer_para.alignment = PP_ALIGN.CENTER

    # Slide 2: Agenda
    slide = prs.slides.add_slide(prs.slide_layouts[1])  # Title and Content
    title = slide.shapes.title
    title.text = "Agenda"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.text = "1. E2E Request Flow Overview"

    for item in [
        "2. Key Components Explained",
        "3. Understanding 502 Errors",
        "4. Debugging Process (Step-by-Step)",
        "5. Common Root Causes",
        "6. Solutions & Best Practices",
        "7. Hardcoding Issue & KVM Solution",
        "8. Next Steps"
    ]:
        p = tf.add_paragraph()
        p.text = item
        p.level = 0
        p.font.size = Pt(24)

    # Slide 3: E2E Request Flow
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "End-to-End Request Flow"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    # Create flow diagram using text boxes
    left = 1.5
    top = 1.8
    width = 7
    height = 0.6
    spacing = 0.8

    flow_items = [
        ("1. User/Client", "api.autozone.com/ai/chatbot", LIGHT_GRAY, DARK_BLUE),
        ("2. DNS Resolution", "Resolves to 35.x.x.x (Apigee IP)", LIGHT_GRAY, DARK_BLUE),
        ("3. Apigee Gateway", "Reads KVM, rewrites path /ai/chatbot → /v2/chat", RGBColor(232, 245, 233), DARK_BLUE),
        ("4. Internal Load Balancer", "Routes to Cloud Run via 10.128.0.5", RGBColor(255, 243, 224), DARK_BLUE),
        ("5. Cloud Run (EUW3/EUW1)", "Processes AI request, returns response", RGBColor(227, 242, 253), DARK_BLUE),
    ]

    for i, (title_text, desc_text, bg_color, text_color) in enumerate(flow_items):
        box = slide.shapes.add_textbox(Inches(left), Inches(top + i * spacing), Inches(width), Inches(height))
        tf = box.text_frame
        tf.text = title_text
        p = tf.paragraphs[0]
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = text_color

        p2 = tf.add_paragraph()
        p2.text = desc_text
        p2.font.size = Pt(14)
        p2.font.color.rgb = text_color

        # Add background
        fill = box.fill
        fill.solid()
        fill.fore_color.rgb = bg_color

        # Add arrow
        if i < len(flow_items) - 1:
            arrow = slide.shapes.add_shape(
                1,  # Line
                Inches(left + width/2 - 0.1),
                Inches(top + i * spacing + height),
                Inches(0.2),
                Inches(spacing - height - 0.05)
            )

    # Slide 4: Key Components - DNS & Base Path
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Key Components (1/3)"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    # DNS
    p = tf.paragraphs[0]
    p.text = "🌐 DNS (Domain Name System)"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    for item in [
        "Converts friendly names to IP addresses",
        "Example: api.autozone.com → 35.x.x.x",
        "Enables geo-routing: EU users → EUW3",
        "Supports failover: EUW3 down → EUW1"
    ]:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    tf.add_paragraph()

    # Base Path
    p = tf.add_paragraph()
    p.text = "📍 Base Path"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    for item in [
        "The URL path users see and call",
        "Example: /ai/chatbot or /v1/recommendation",
        "Provides clean, consistent API for consumers",
        "Backend can change without affecting users"
    ]:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    # Slide 5: Key Components - Target Path & KVM
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Key Components (2/3)"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    # Target Path
    p = tf.paragraphs[0]
    p.text = "🎯 Target Path"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    for item in [
        "The actual path on your backend service",
        "Apigee rewrites: /ai/chatbot → /v2/chat",
        "Current issue: Hardcoded paths in Dev/QA vs Prod",
        "Solution: Use KVM for dynamic configuration"
    ]:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    tf.add_paragraph()

    # KVM
    p = tf.add_paragraph()
    p.text = "🗄️ KVM (Key-Value Maps)"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    for item in [
        "Secure storage for environment-specific settings",
        "No hardcoding in proxy code",
        "Change values without redeploying proxy",
        "Different values per environment (Dev/QA/Prod)"
    ]:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    # Slide 6: Key Components - ILB & Target Server
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Key Components (3/3)"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    # ILB
    p = tf.paragraphs[0]
    p.text = "⚖️ Internal Load Balancer (ILB)"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    for item in [
        "Provides stable internal endpoint for Cloud Run",
        "Distributes traffic across multiple instances",
        "Enables private connectivity (not public internet)",
        "Config: EUW3 (80%) + EUW1 (20%) traffic split"
    ]:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    tf.add_paragraph()

    # Target Backend Server
    p = tf.add_paragraph()
    p.text = "🖥️ Target Backend Server"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    for item in [
        "Where Apigee actually sends the request",
        "Configured in Apigee: Host, Port, SSL settings",
        "Multi-region: Primary (EUW3) + Secondary (EUW1)",
        "Load balancing based on health checks & policies"
    ]:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    # Slide 7: Understanding 502 Errors
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Understanding 502 Bad Gateway"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    # Add explanation box
    box = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(1.5))
    tf = box.text_frame
    p = tf.paragraphs[0]
    p.text = "What Does 502 Mean?"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    p = tf.add_paragraph()
    p.text = "✅ Request reached ILB successfully"
    p.font.size = Pt(22)
    p.font.color.rgb = RGBColor(0, 128, 0)

    p = tf.add_paragraph()
    p.text = "❌ ILB couldn't get valid response from Cloud Run"
    p.font.size = Pt(22)
    p.font.color.rgb = RGBColor(255, 0, 0)

    # Add location box
    box2 = slide.shapes.add_textbox(Inches(1), Inches(4), Inches(8), Inches(2))
    tf2 = box2.text_frame
    p = tf2.paragraphs[0]
    p.text = "Where the Problem Occurs:"
    p.font.size = Pt(24)
    p.font.bold = True

    p = tf2.add_paragraph()
    p.text = "User → DNS → Apigee → ILB → Cloud Run"
    p.font.size = Pt(20)
    p.font.color.rgb = DARK_BLUE

    p = tf2.add_paragraph()
    p.text = "                                    ↑"
    p.font.size = Pt(20)
    p.font.color.rgb = RGBColor(255, 0, 0)

    p = tf2.add_paragraph()
    p.text = "                         502 happens here"
    p.font.size = Pt(20)
    p.font.color.rgb = RGBColor(255, 0, 0)
    p.font.bold = True

    # Slide 8: Debugging Process - Overview
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Debugging Process: 10-Step Checklist"
    title.text_frame.paragraphs[0].font.size = Pt(36)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    checklist = [
        "1. Check Apigee Trace - What URL/error?",
        "2. Check ILB backend health status",
        "3. Check Cloud Run logs - Are requests arriving?",
        "4. Check Cloud Run service status - Is it running?",
        "5. Check timeout chain - ILB > Cloud Run?",
        "6. Check firewall rules - Is traffic allowed?",
        "7. Check VPC connector - Cloud Run connected?",
        "8. Check health check endpoint - /health exists?",
        "9. Check protocol match - HTTP vs HTTPS?",
        "10. Test direct curl from VPC"
    ]

    p = tf.paragraphs[0]
    p.text = checklist[0]
    p.font.size = Pt(18)

    for item in checklist[1:]:
        p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(18)

    # Slide 9: Step 1 - Apigee Trace
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Step 1: Check Apigee Trace"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    p = tf.paragraphs[0]
    p.text = "Why: Captures full request/response flow"
    p.font.size = Pt(20)
    p.font.bold = True

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "Key Variables to Check:"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    trace_vars = [
        "target.url - What URL did Apigee call?",
        "target.host - Correct backend server?",
        "target.port - Usually 443 for Cloud Run",
        "target.error.message - Actual error from backend",
        "response.status.code - 502",
        "upstream.response.time - Timeout duration?"
    ]

    for item in trace_vars:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    # Slide 10: Step 2 - ILB Health Checks
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Step 2: Check ILB Health Checks"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    p = tf.paragraphs[0]
    p.text = "Why: ILB marks backends unhealthy if they fail checks"
    p.font.size = Pt(20)
    p.font.bold = True

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "Common Issues:"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    health_issues = [
        "❌ Health check path wrong: /health vs /healthz",
        "❌ Health check timeout too short",
        "❌ Cloud Run not responding to health checks",
        "❌ Health check port mismatch (80 vs 443)"
    ]

    for item in health_issues:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "Command:"
    p.font.size = Pt(18)
    p.font.bold = True

    p = tf.add_paragraph()
    p.text = "gcloud compute backend-services get-health [ILB-NAME] --region=europe-west3"
    p.font.size = Pt(14)
    p.font.name = "Courier New"

    # Slide 11: Step 3 - Cloud Run Logs
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Step 3: Check Cloud Run Logs"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    p = tf.paragraphs[0]
    p.text = "Why: See if requests arrive & what errors occur"
    p.font.size = Pt(20)
    p.font.bold = True

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "Common Error Patterns:"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    log_errors = [
        '"connection refused" → Cloud Run not listening on port',
        '"upstream timeout" → Request taking too long',
        '"out of memory" → Container crashed',
        '"container failed to start" → Image/startup issue',
        'No logs at all → Traffic not reaching Cloud Run'
    ]

    for item in log_errors:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    # Slide 12: Timeout Chain Analysis
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Critical: Timeout Chain Analysis"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    # Add table-like structure
    box = slide.shapes.add_textbox(Inches(1.5), Inches(2), Inches(7), Inches(4))
    tf = box.text_frame

    p = tf.paragraphs[0]
    p.text = "⚠️ THE RULE: Each layer timeout must be > next layer's timeout"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 0, 0)

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "Component                   Timeout          Recommended"
    p.font.size = Pt(16)
    p.font.name = "Courier New"
    p.font.bold = True

    timeout_chain = [
        "User/Browser                120s             N/A",
        "Apigee Proxy                60s (default)    120s+",
        "ILB Backend                 30s (default)    300s+",
        "Cloud Run                   300s (default)   300s",
        "AI Model                    Actual: 45s      N/A"
    ]

    for item in timeout_chain:
        p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(16)
        p.font.name = "Courier New"

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "🚨 Most common 502 cause: ILB timeout (30s) < Cloud Run processing (45s)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    # Slide 13: Common Root Causes
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Common 502 Root Causes (By Frequency)"
    title.text_frame.paragraphs[0].font.size = Pt(36)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    causes = [
        ("1. Timeout Mismatch (60%)", "ILB timeout < Cloud Run processing time", "Increase ILB timeout to 300s"),
        ("2. Unhealthy Backend (20%)", "Health check fails → backend marked unhealthy", "Fix health check endpoint or thresholds"),
        ("3. Cloud Run Cold Start (10%)", "No min instances → cold start takes too long", "Set minScale: 1 on Cloud Run"),
        ("4. Network/Firewall (5%)", "Firewall blocks ILB → Cloud Run traffic", "Add firewall rule allowing ILB subnet"),
        ("5. Wrong Target Config (5%)", "Apigee points to old ILB IP", "Update Apigee target server")
    ]

    p = tf.paragraphs[0]
    p.text = causes[0][0]
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    for item in [causes[0][1], causes[0][2]]:
        p = tf.add_paragraph()
        p.text = f"   {item}"
        p.font.size = Pt(14)

    for cause, symptom, fix in causes[1:]:
        tf.add_paragraph()
        p = tf.add_paragraph()
        p.text = cause
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = AUTOZONE_ORANGE

        for item in [symptom, fix]:
            p = tf.add_paragraph()
            p.text = f"   {item}"
            p.font.size = Pt(14)

    # Slide 14: Hardcoding Problem
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Current Issue: Hardcoded Paths"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    # Problem box
    box1 = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(1.5))
    tf1 = box1.text_frame
    p = tf1.paragraphs[0]
    p.text = "❌ Current Approach (Hardcoded)"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 0, 0)

    p = tf1.add_paragraph()
    p.text = 'if (environment == "prod") {'
    p.font.size = Pt(16)
    p.font.name = "Courier New"

    p = tf1.add_paragraph()
    p.text = '  targetPath = "/multi-region/ai-service";'
    p.font.size = Pt(16)
    p.font.name = "Courier New"

    p = tf1.add_paragraph()
    p.text = '} else {'
    p.font.size = Pt(16)
    p.font.name = "Courier New"

    p = tf1.add_paragraph()
    p.text = '  targetPath = "/europe-west3/ai-service";'
    p.font.size = Pt(16)
    p.font.name = "Courier New"

    p = tf1.add_paragraph()
    p.text = '}'
    p.font.size = Pt(16)
    p.font.name = "Courier New"

    fill1 = box1.fill
    fill1.solid()
    fill1.fore_color.rgb = RGBColor(255, 230, 230)

    # Issues list
    box2 = slide.shapes.add_textbox(Inches(1), Inches(4), Inches(8), Inches(2))
    tf2 = box2.text_frame
    p = tf2.paragraphs[0]
    p.text = "Problems:"
    p.font.size = Pt(20)
    p.font.bold = True

    issues = [
        "Different code for different environments",
        "Requires code change to update paths",
        "Deployment needed for configuration changes",
        "Doesn't scale for multiple regions"
    ]

    for issue in issues:
        p = tf2.add_paragraph()
        p.text = f"• {issue}"
        p.font.size = Pt(16)

    # Slide 15: KVM Solution
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Solution: Use KVM (Key-Value Maps)"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    # Solution box
    box1 = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(1.2))
    tf1 = box1.text_frame
    p = tf1.paragraphs[0]
    p.text = "✅ Recommended Approach (KVM)"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0, 128, 0)

    p = tf1.add_paragraph()
    p.text = 'var region = context.getVariable("kvm.region_path");'
    p.font.size = Pt(16)
    p.font.name = "Courier New"

    p = tf1.add_paragraph()
    p.text = 'var targetPath = "/services/" + region + "/ai";'
    p.font.size = Pt(16)
    p.font.name = "Courier New"

    fill1 = box1.fill
    fill1.solid()
    fill1.fore_color.rgb = RGBColor(230, 255, 230)

    # KVM Config
    box2 = slide.shapes.add_textbox(Inches(1), Inches(3.7), Inches(8), Inches(1.5))
    tf2 = box2.text_frame
    p = tf2.paragraphs[0]
    p.text = "KVM Configuration per Environment:"
    p.font.size = Pt(18)
    p.font.bold = True

    kvm_config = [
        "Dev:   region_path = 'europe-west3'",
        "QA:    region_path = 'europe-west3'",
        "Stage: region_path = 'multi-region'",
        "Prod:  region_path = 'multi-region'"
    ]

    for config in kvm_config:
        p = tf2.add_paragraph()
        p.text = config
        p.font.size = Pt(16)
        p.font.name = "Courier New"

    # Benefits
    box3 = slide.shapes.add_textbox(Inches(1), Inches(5.5), Inches(8), Inches(1.5))
    tf3 = box3.text_frame
    p = tf3.paragraphs[0]
    p.text = "Benefits:"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    benefits = [
        "✅ No code changes between environments",
        "✅ Easy to update (just change KVM value)",
        "✅ No redeployment needed",
        "✅ Consistent structure across all environments"
    ]

    for benefit in benefits:
        p = tf3.add_paragraph()
        p.text = benefit
        p.font.size = Pt(14)

    # Slide 16: Debug Script
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Quick Debug Script"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    p = tf.paragraphs[0]
    p.text = "PowerShell script to check all critical components:"
    p.font.size = Pt(18)

    tf.add_paragraph()

    script_steps = [
        "1. Cloud Run service status",
        "2. Cloud Run recent errors (last 10 min)",
        "3. ILB backend health",
        "4. ILB timeout configuration",
        "5. VPC connector status",
        "6. Firewall rules"
    ]

    for step in script_steps:
        p = tf.add_paragraph()
        p.text = step
        p.font.size = Pt(20)
        p.level = 1

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "Script available: debug-502.ps1"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    # Slide 17: Multi-Region Architecture
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Multi-Region Architecture"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    # Create architecture diagram using shapes
    # EUW3 Region
    box_euw3 = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(3.5), Inches(3))
    tf_euw3 = box_euw3.text_frame
    p = tf_euw3.paragraphs[0]
    p.text = "Europe-West3 (Primary)"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.alignment = PP_ALIGN.CENTER

    for item in ["", "Apigee Gateway", "↓", "ILB (10.128.0.5)", "↓", "Cloud Run AI", "80% Traffic"]:
        p = tf_euw3.add_paragraph()
        p.text = item
        p.font.size = Pt(14)
        p.alignment = PP_ALIGN.CENTER

    fill_euw3 = box_euw3.fill
    fill_euw3.solid()
    fill_euw3.fore_color.rgb = RGBColor(227, 242, 253)

    # EUW1 Region
    box_euw1 = slide.shapes.add_textbox(Inches(5.5), Inches(2.5), Inches(3.5), Inches(3))
    tf_euw1 = box_euw1.text_frame
    p = tf_euw1.paragraphs[0]
    p.text = "Europe-West1 (Secondary)"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.alignment = PP_ALIGN.CENTER

    for item in ["", "Apigee Gateway", "↓", "ILB (10.129.0.5)", "↓", "Cloud Run AI", "20% Traffic"]:
        p = tf_euw1.add_paragraph()
        p.text = item
        p.font.size = Pt(14)
        p.alignment = PP_ALIGN.CENTER

    fill_euw1 = box_euw1.fill
    fill_euw1.solid()
    fill_euw1.fore_color.rgb = RGBColor(241, 248, 233)

    # DNS at top
    box_dns = slide.shapes.add_textbox(Inches(3), Inches(1.5), Inches(4), Inches(0.6))
    tf_dns = box_dns.text_frame
    p = tf_dns.paragraphs[0]
    p.text = "Cloud DNS (Geo-routing)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER

    fill_dns = box_dns.fill
    fill_dns.solid()
    fill_dns.fore_color.rgb = RGBColor(255, 244, 225)

    # Slide 18: Next Steps
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Next Steps & Recommendations"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    p = tf.paragraphs[0]
    p.text = "Immediate Actions"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    immediate = [
        "Replace hardcoded paths with KVM",
        "Set up monitoring alerts for ILB health",
        "Document runbook for on-call team",
        "Test failover scenarios (EUW3 → EUW1)"
    ]

    for item in immediate:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "Long-term Improvements"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    longterm = [
        "Automated health monitoring & alerting",
        "SLO/SLA tracking (99.9% availability)",
        "Load testing for timeout configurations",
        "Comprehensive disaster recovery plan"
    ]

    for item in longterm:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    # Slide 19: Resources & Contact
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    title.text = "Resources & Escalation"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE

    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()

    p = tf.paragraphs[0]
    p.text = "For 502 Issues:"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    for item in ["1. Check debugging guide", "2. Run debug script: debug-502.ps1", "3. Review Apigee trace + Cloud Run logs", "4. Escalate to Platform Team / SRE"]:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "For Configuration Changes:"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    for item in ["KVM updates: Apigee Admin", "ILB changes: Network Team", "Cloud Run changes: Cloud Platform Team"]:
        p = tf.add_paragraph()
        p.text = item
        p.level = 1
        p.font.size = Pt(18)

    tf.add_paragraph()

    p = tf.add_paragraph()
    p.text = "Documentation:"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = AUTOZONE_ORANGE

    p = tf.add_paragraph()
    p.text = "apigee-502-debugging-guide.md"
    p.level = 1
    p.font.size = Pt(18)

    # Slide 20: Thank You
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank

    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BLUE

    # Title
    thank_box = slide.shapes.add_textbox(Inches(0.5), Inches(3), Inches(9), Inches(1.5))
    thank_frame = thank_box.text_frame
    thank_frame.text = "Thank You"
    thank_para = thank_frame.paragraphs[0]
    thank_para.font.size = Pt(54)
    thank_para.font.bold = True
    thank_para.font.color.rgb = WHITE
    thank_para.alignment = PP_ALIGN.CENTER

    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.5), Inches(9), Inches(1))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = "Questions?"
    subtitle_para = subtitle_frame.paragraphs[0]
    subtitle_para.font.size = Pt(36)
    subtitle_para.font.color.rgb = AUTOZONE_ORANGE
    subtitle_para.alignment = PP_ALIGN.CENTER

    return prs

def main():
    print("🎨 Generating PowerPoint presentation...")
    prs = create_presentation()

    output_file = "apigee-502-debugging-presentation.pptx"
    prs.save(output_file)
    print(f"✅ Presentation created successfully: {output_file}")
    print(f"   Total slides: {len(prs.slides)}")

if __name__ == "__main__":
    main()
