"""
Generate PowerPoint Presentation for Diagnostic Intelligence Cost Analysis
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
import os

# AutoZone brand colors
AUTOZONE_ORANGE = RGBColor(255, 102, 0)  # #FF6600
AUTOZONE_BLACK = RGBColor(0, 0, 0)
AUTOZONE_GRAY = RGBColor(102, 102, 102)
WHITE = RGBColor(255, 255, 255)
LIGHT_GRAY = RGBColor(240, 240, 240)
GREEN = RGBColor(0, 176, 80)
RED = RGBColor(255, 0, 0)

def create_title_slide(prs):
    """Slide 1: Title Slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout

    # Orange header bar
    header = slide.shapes.add_shape(
        1,  # Rectangle
        Inches(0), Inches(0), Inches(10), Inches(1.5)
    )
    header.fill.solid()
    header.fill.fore_color.rgb = AUTOZONE_ORANGE
    header.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(1.2))
    tf = title_box.text_frame
    tf.text = "ALLDATA Diagnostic Intelligence"
    p = tf.paragraphs[0]
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(9), Inches(0.8))
    tf = subtitle_box.text_frame
    tf.text = "AI Model Cost Comparison Analysis\nGemini 2.5 Pro vs Flash Deployment Strategies"
    p = tf.paragraphs[0]
    p.font.size = Pt(24)
    p.font.color.rgb = AUTOZONE_GRAY
    p.alignment = PP_ALIGN.CENTER

    # Date and details
    details_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.5), Inches(9), Inches(1))
    tf = details_box.text_frame
    tf.text = "August 6, 2026\n\nCMDB Application: ALLDATA Diagnostic Intelligence\nCMDB Global ID: 49533b7e773064d48e7adabaaf81dba5"
    p = tf.paragraphs[0]
    p.font.size = Pt(14)
    p.font.color.rgb = AUTOZONE_GRAY
    p.alignment = PP_ALIGN.CENTER

    return slide

def add_title_content_slide(prs, title_text, content_lines):
    """Helper to create a standard title + content slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])  # Title only layout

    # Title
    title = slide.shapes.title
    title.text = title_text
    title.text_frame.paragraphs[0].font.size = Pt(32)
    title.text_frame.paragraphs[0].font.bold = True
    title.text_frame.paragraphs[0].font.color.rgb = AUTOZONE_ORANGE

    # Content
    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(5))
    tf = content_box.text_frame
    tf.word_wrap = True

    for line in content_lines:
        p = tf.add_paragraph()
        p.text = line
        p.font.size = Pt(14)
        p.space_before = Pt(6)
        p.space_after = Pt(6)

    return slide

def add_table_slide(prs, title_text, headers, rows):
    """Helper to create a slide with a table"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    # Title
    title = slide.shapes.title
    title.text = title_text
    title.text_frame.paragraphs[0].font.size = Pt(32)
    title.text_frame.paragraphs[0].font.bold = True
    title.text_frame.paragraphs[0].font.color.rgb = AUTOZONE_ORANGE

    # Table
    rows_count = len(rows) + 1  # +1 for header
    cols_count = len(headers)

    left = Inches(0.5)
    top = Inches(2)
    width = Inches(9)
    height = Inches(0.5) * rows_count

    table = slide.shapes.add_table(rows_count, cols_count, left, top, width, height).table

    # Header row
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = AUTOZONE_ORANGE
        cell.text_frame.paragraphs[0].font.color.rgb = WHITE
        cell.text_frame.paragraphs[0].font.bold = True
        cell.text_frame.paragraphs[0].font.size = Pt(12)

    # Data rows
    for row_idx, row in enumerate(rows):
        for col_idx, cell_text in enumerate(row):
            cell = table.cell(row_idx + 1, col_idx)
            cell.text = str(cell_text)
            cell.text_frame.paragraphs[0].font.size = Pt(11)

            # Alternating row colors
            if row_idx % 2 == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_GRAY

    return slide

def create_presentation():
    """Create the complete PowerPoint presentation"""
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Slide 1: Title
    create_title_slide(prs)

    # Slide 2: Executive Summary
    add_table_slide(
        prs,
        "Executive Summary",
        ["Metric", "Scenario A", "Scenario B"],
        [
            ["Lower Environments", "Gemini 2.5 Pro", "Gemini 2.5 Flash"],
            ["Production (NA + EU)", "Gemini 2.5 Flash", "Gemini 2.5 Pro"],
            ["Monthly Cost", "$2,407", "$3,157"],
            ["With Cache (75% hit)", "~$602", "~$789"],
            ["Cost Difference", "Baseline", "+$749/month (+31%)"],
            ["Recommendation", "", "✅ Scenario B"]
        ]
    )

    # Slide 3: Background & Context
    add_title_content_slide(
        prs,
        "Background & Context",
        [
            "📋 ALLDATA Diagnostic Intelligence - AI Assist",
            "",
            "🎯 Problem Statement:",
            "   • Technicians need access to diagnostic insights from Gemini@AutoZone LLM",
            "",
            "💼 Business Benefits:",
            "   • Increase revenue through subscription-based AI-enhanced diagnostic tool",
            "   • Position ALLDATA as industry leader in AI-assisted automotive diagnostics",
            "   • Reduce diagnosis time with comprehensive diagnostic information",
            "   • Improve customer retention with one-stop DTC diagnosis solution",
            "",
            "📅 Current Status:",
            "   • ⭐ Phase 1 Production Complete (North America)",
            "   • 🚀 Phase 2 Europe Expansion: Q4 FY26 - Q2 FY27"
        ]
    )

    # Slide 4: System Architecture
    add_title_content_slide(
        prs,
        "System Architecture Overview",
        [
            "☁️ Cloud-Native Serverless Architecture:",
            "",
            "   [Technician] → [Akamai CDN] → [Ping Auth] → [APIGEE Gateway]",
            "       → [Internal Load Balancer] → [Cloud Run - DI-AI Answers]",
            "           → [AlloyDB Cache Check]",
            "               → Cache Hit? → Return cached response",
            "               → Cache Miss → [Vertex AI Gemini 2.5]",
            "                   → Save to AlloyDB → Return diagnostic report",
            "",
            "🔑 Key Components:",
            "   • Cloud Run: Auto-scaling serverless compute",
            "   • AlloyDB: PostgreSQL-based cache (30-day validity)",
            "   • Vertex AI: Gemini model access",
            "   • Cache Strategy: Reduces AI API costs by 70-80%",
            "",
            "⚡ Quality Attributes:",
            "   • Response Time SLA: 60 seconds",
            "   • Request Size: ~100 Bytes | Response Size: ~6KB"
        ]
    )

    # Slide 5: Model Comparison
    add_table_slide(
        prs,
        "Gemini 2.5 Pro vs Flash Comparison",
        ["Feature", "Gemini 2.5 Pro", "Gemini 2.5 Flash"],
        [
            ["Input Pricing", "$1.25 / 1M tokens", "$0.30 / 1M tokens"],
            ["Output Pricing", "$10.00 / 1M tokens", "$2.50 / 1M tokens"],
            ["Cost Ratio", "4.2x more expensive", "Baseline"],
            ["Diagnostic Accuracy", "⭐⭐⭐⭐⭐ Excellent", "⭐⭐⭐⭐ Very Good"],
            ["Complex Cases", "Superior handling", "Good for common DTCs"],
            ["Response Quality", "Comprehensive, detailed", "Fast, concise"],
            ["Best Use Case", "Production - paying customers", "Testing, common scenarios"],
            ["Deprecation", "⚠️ Oct 16, 2026", "⚠️ Oct 16, 2026"]
        ]
    )

    # Slide 6: Traffic Estimates
    add_table_slide(
        prs,
        "Traffic & Token Estimates",
        ["Environment", "Requests/Month", "Purpose"],
        [
            ["Prod - North America", "150,000", "Live customer traffic"],
            ["Prod - Europe", "50,000", "Phase 2 expansion"],
            ["Stage", "25,000", "Pre-production testing"],
            ["QA", "10,000", "Integration testing"],
            ["Dev", "5,000", "Development testing"],
            ["TOTAL", "240,000", ""]
        ]
    )

    # Slide 7: Scenario A Costs
    add_table_slide(
        prs,
        "Scenario A: Pro for Lower, Flash for Prod",
        ["Environment/Region", "Model", "Monthly Cost"],
        [
            ["Dev", "Gemini 2.5 Pro", "$1,130"],
            ["QA", "Gemini 2.5 Pro", "$376"],
            ["Stage", "Gemini 2.5 Pro", "$150"],
            ["Lower Envs Subtotal", "", "$1,656"],
            ["", "", ""],
            ["Prod - North America", "Gemini 2.5 Flash", "$564"],
            ["Prod - Europe", "Gemini 2.5 Flash", "$188"],
            ["Production Subtotal", "", "$752"],
            ["", "", ""],
            ["TOTAL MONTHLY", "", "$2,407"],
            ["ANNUAL", "", "$28,887"]
        ]
    )

    # Slide 8: Scenario B Costs
    add_table_slide(
        prs,
        "Scenario B: Flash for Lower, Pro for Prod ⭐",
        ["Environment/Region", "Model", "Monthly Cost"],
        [
            ["Dev", "Gemini 2.5 Flash", "$19"],
            ["QA", "Gemini 2.5 Flash", "$38"],
            ["Stage", "Gemini 2.5 Flash", "$94"],
            ["Lower Envs Subtotal", "", "$151"],
            ["", "", ""],
            ["Prod - North America", "Gemini 2.5 Pro", "$2,255"],
            ["Prod - Europe", "Gemini 2.5 Pro", "$752"],
            ["Production Subtotal", "", "$3,006"],
            ["", "", ""],
            ["TOTAL MONTHLY", "", "$3,157"],
            ["ANNUAL", "", "$37,879"]
        ]
    )

    # Slide 9: Cost Comparison
    add_table_slide(
        prs,
        "Side-by-Side Cost Comparison",
        ["Component", "Scenario A", "Scenario B", "Difference"],
        [
            ["Lower Environments", "$1,656", "$151", "-$1,505 (-91%) ✅"],
            ["Production", "$752", "$3,006", "+$2,255 (+300%)"],
            ["TOTAL MONTHLY", "$2,407", "$3,157", "+$749 (+31%)"],
            ["ANNUAL", "$28,887", "$37,879", "+$8,991 (+31%)"]
        ]
    )

    # Slide 10: Cache Impact
    add_table_slide(
        prs,
        "Cache Impact Analysis",
        ["Scenario", "Uncached Cost", "Cache Hit Rate", "Effective Monthly"],
        [
            ["Scenario A", "$2,407", "75%", "~$602"],
            ["Scenario B", "$3,157", "75%", "~$789"],
            ["Difference", "", "", "~$187/month"]
        ]
    )

    # Slide 11: Quality Analysis
    add_title_content_slide(
        prs,
        "Quality vs. Cost Analysis",
        [
            "✅ Gemini 2.5 Pro Advantages (Production):",
            "",
            "🎯 Superior diagnostic accuracy - Better at complex automotive troubleshooting",
            "📋 More comprehensive responses - Detailed probable causes, diagnostic procedures",
            "🧠 Better contextual understanding - Handles edge cases and rare DTCs effectively",
            "⚡ Reduced technician time - Higher quality = faster problem resolution",
            "",
            "💼 Business Impact:",
            "   • Supports premium subscription model",
            "   • Competitive differentiation in market",
            "   • Aligns with 'industry leader' positioning",
            "   • Mitigates HLD risk: 'less accurate LLM responses'",
            "",
            "✅ Gemini 2.5 Flash Advantages (Lower Environments):",
            "",
            "💰 91% cost savings on testing environments",
            "⚡ Faster development cycles - No budget constraints",
            "✅ Adequate quality for development and QA validation"
        ]
    )

    # Slide 12: Regional Breakdown
    add_table_slide(
        prs,
        "Regional Cost Breakdown",
        ["Region", "Traffic/Month", "Scenario A (Flash)", "Scenario B (Pro)", "Premium"],
        [
            ["North America", "150,000", "$564", "$2,255", "+$1,691"],
            ["Europe (Phase 2)", "50,000", "$188", "$752", "+$564"],
            ["TOTAL", "200,000", "$752", "$3,006", "+$2,255"]
        ]
    )

    # Slide 13: Risk Assessment
    add_table_slide(
        prs,
        "Risk Assessment - Financial",
        ["Risk", "Impact", "Mitigation Strategy"],
        [
            ["Traffic exceeds estimates", "Cost overruns", "Rate limiting, budget alerts at 80%/95%"],
            ["Low cache hit rate", "Higher AI costs", "Optimize cache, extend validity to 60-90 days"],
            ["Model deprecation", "Migration costs", "Plan Gemini 3.x migration Q3 FY26"]
        ]
    )

    # Slide 14: Cost Optimization
    add_title_content_slide(
        prs,
        "Cost Optimization Strategies",
        [
            "💾 1. Cache Optimization",
            "   • Current: 30-day cache validity",
            "   • Recommendation: Extend to 60-90 days for stable DTC patterns",
            "   • Potential savings: +10-15% reduction in API calls",
            "",
            "📊 2. Batch Processing for Analytics",
            "   • Use case: Non-real-time diagnostic pattern analysis",
            "   • Batch API pricing: 50% discount",
            "   • Application: Historical data analysis, trend reporting",
            "",
            "🔀 3. Hybrid Routing (Advanced)",
            "   • Common DTCs (80%) → Flash model",
            "   • Complex/rare DTCs (20%) → Pro model",
            "   • Estimated savings: 40-50% vs. Pro-only deployment",
            "   • Implementation: Q2-Q3 FY27",
            "",
            "💡 4. Flash-Lite for Dev Environment",
            "   • Use Gemini 2.5 Flash-Lite for Dev only",
            "   • Additional savings: ~$15-20/month"
        ]
    )

    # Slide 15: Recommendations
    add_title_content_slide(
        prs,
        "⭐ Recommendation: Scenario B",
        [
            "Deploy Gemini 2.5 Flash for Lower Environments, Pro for Production",
            "",
            "🎯 1. Quality Where It Matters",
            "   • Production users receive highest quality diagnostic information",
            "   • Accuracy directly impacts revenue and customer satisfaction",
            "",
            "💰 2. Cost-Effective Testing",
            "   • 91% savings on lower environments ($1,505/month)",
            "   • Enables unlimited testing without budget constraints",
            "",
            "💵 3. Manageable Premium",
            "   • $749/month premium (31% increase)",
            "   • With caching: Only ~$187/month effective cost difference",
            "",
            "⚠️ 4. Risk Mitigation",
            "   • HLD identifies 'less accurate LLM responses' as a risk",
            "   • Pro model in production addresses this concern",
            "",
            "🚀 5. Future-Proof",
            "   • Enables hybrid routing optimization later (40-50% savings)",
            "   • Supports premium pricing model"
        ]
    )

    # Slide 16: Budget Recommendation
    add_table_slide(
        prs,
        "Budget Recommendation",
        ["Phase", "Timeline", "Monthly Budget", "Annual Budget"],
        [
            ["Phase 1 (NA only)", "Current", "$800 - $1,000", "$10,000 - $12,000"],
            ["Phase 2 (NA + EU)", "Q1-Q2 FY27", "$3,200 - $3,500", "$38,000 - $42,000"],
            ["Total Infrastructure", "Full deployment", "$4,000 - $5,000", "$48,000 - $60,000"]
        ]
    )

    # Slide 17: Implementation Roadmap
    add_title_content_slide(
        prs,
        "Implementation Roadmap",
        [
            "⚡ Phase 1: Immediate Actions (Q4 FY26) - Weeks 1-4",
            "   ✅ Week 1-2: Deploy Scenario B configuration",
            "   ✅ Week 3-4: Set up monitoring dashboards and budget alerts",
            "",
            "📊 Phase 2: Short-term Optimization (Q1 FY27) - Months 2-4",
            "   📈 Analyze cache hit rates and optimize",
            "   🧪 A/B test Flash vs Pro (10% traffic split)",
            "   🔍 Evaluate Gemini 3.x migration path",
            "",
            "🚀 Phase 3: Advanced Optimization (Q2-Q3 FY27) - Months 5-9",
            "   🤖 Implement hybrid routing (Flash for common, Pro for complex)",
            "   🔄 Complete Gemini 3.x migration (before Oct 2026 deadline)",
            "   📊 Quarterly cost optimization reviews",
            "",
            "🎯 Key Milestones:",
            "   • Q4 FY26: Budget approval and deployment",
            "   • Q1 FY27: Europe soft launch",
            "   • Q2 FY27: Europe full production",
            "   • Q3 FY27: Gemini 3.x migration complete"
        ]
    )

    # Slide 18: Success Metrics
    add_table_slide(
        prs,
        "Success Metrics & KPIs",
        ["Category", "KPI", "Target", "Frequency"],
        [
            ["Cost 💰", "Monthly AI Cost", "< $900 (Phase 1)", "Weekly"],
            ["Cost 💰", "Cost per Request", "< $0.005", "Monthly"],
            ["Cost 💰", "Cache Hit Rate", "> 75%", "Daily"],
            ["Quality 🎯", "Diagnostic Accuracy", "> 90%", "Weekly"],
            ["Quality 🎯", "Response Time SLA", "< 60 seconds", "Real-time"],
            ["Quality 🎯", "Technician Satisfaction", "> 4.5/5.0", "Quarterly"],
            ["Business 📈", "Subscription Revenue", "+15% YoY", "Quarterly"],
            ["Business 📈", "Customer Retention", "> 95%", "Monthly"]
        ]
    )

    # Slide 19: Sensitivity Analysis
    add_table_slide(
        prs,
        "Sensitivity Analysis - Traffic Scenarios",
        ["Scenario", "Traffic", "Scenario A", "Scenario B", "Difference"],
        [
            ["Conservative (50%)", "120K/month", "$1,204", "$1,578", "+$375"],
            ["Base Case (100%)", "240K/month", "$2,407", "$3,157", "+$749"],
            ["Aggressive (200%)", "480K/month", "$4,815", "$6,313", "+$1,499"]
        ]
    )

    # Slide 20: Competitive Context
    add_title_content_slide(
        prs,
        "Competitive Analysis Context",
        [
            "🏆 ALLDATA's Market Position:",
            "   • Industry leader in automotive diagnostic data",
            "   • Subscription-based revenue model",
            "   • Target: Professional automotive technicians",
            "",
            "🎯 Competitive Landscape:",
            "   • Mitchell 1: Limited AI features (Basic)",
            "   • Identifix: Traditional troubleshooting (Non-AI)",
            "   • Chilton/Haynes: No AI integration",
            "   • ALLDATA: ✅ Gemini-powered (Industry-leading)",
            "",
            "💡 Differentiation Strategy:",
            '   "Position ALLDATA as industry leader in AI-assisted automotive diagnostics"',
            "",
            "   • Quality over cost maintains competitive advantage",
            "   • Pro model delivers on brand promise",
            "   • Premium experience justifies subscription pricing",
            "   • First-mover advantage in AI-powered diagnostics",
            "",
            "📊 Market Opportunity:",
            "   $749/month premium protects multi-million dollar subscription revenue"
        ]
    )

    # Slide 21: Next Steps
    add_title_content_slide(
        prs,
        "Next Steps & Decision Points",
        [
            "⚡ Immediate Decision Required:",
            "   ☑️ Scenario B: Flash for Lower Envs, Pro for Production - RECOMMENDED",
            "   ☐ Scenario A: Pro for Lower Envs, Flash for Production",
            "",
            "📅 Q4 FY26 (Current Quarter):",
            "   • Finalize budget approval for Scenario B",
            "   • Deploy selected configuration",
            "   • Set up monitoring dashboards",
            "   • Begin Europe Phase 2 planning",
            "",
            "📅 Q1 FY27:",
            "   • Complete 1-month production performance review",
            "   • Initiate A/B testing program",
            "   • Europe soft launch (limited availability)",
            "   • Gemini 3.x migration planning kickoff",
            "",
            "📅 Q2-Q3 FY27:",
            "   • Europe full production release",
            "   • Implement hybrid routing in production",
            "   • Complete Gemini 3.x migration (before Oct 2026)",
            "   • Quarterly cost optimization review"
        ]
    )

    # Slide 22: Q&A
    add_title_content_slide(
        prs,
        "Questions & Discussion",
        [
            "💬 Open Discussion Topics:",
            "",
            "1. Budget Approval",
            "   • Is the $749/month premium acceptable for quality improvement?",
            "   • Any concerns about Phase 2 (EU) budget scaling?",
            "",
            "2. Quality vs. Cost Trade-offs",
            "   • Alignment with product vision and market positioning?",
            "   • Risk tolerance for diagnostic accuracy?",
            "",
            "3. Timeline & Implementation",
            "   • Any constraints on Q4 FY26 deployment?",
            "   • Resource availability for monitoring setup?",
            "",
            "4. Future Considerations",
            "   • Interest in hybrid routing exploration?",
            "   • Gemini 3.x migration timeline concerns?",
            "",
            "",
            "📧 Contact: Technical Program Manager - ALLDATA Diagnostic Intelligence",
            "📄 Supporting Documents: Detailed Cost Analysis Report, HLD v006"
        ]
    )

    # Save presentation
    output_path = r"c:\Users\rkumar\OneDrive - AutoZone Parts, Inc\Desktop\Interface-to-Desktop\FoodforClaude\JiraProject-Summary\output\Diagnostic-Intelligence-AI-Cost-Analysis.pptx"
    prs.save(output_path)
    print(f"✅ Presentation created successfully!")
    print(f"📍 Location: {output_path}")
    print(f"📊 Total slides: {len(prs.slides)}")

if __name__ == "__main__":
    create_presentation()
