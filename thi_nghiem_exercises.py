"""
Script phụ trợ HỌC TẬP — KHÔNG nằm trong bài nộp, có thể xóa sau khi dùng.

Mục đích: chạy sẵn các "thí nghiệm" mà exercises.md yêu cầu, để bạn NHÌN kết quả
thật rồi tự viết câu trả lời bằng lời của mình.

Cách chạy (trong thư mục lab, đã tạo .env với API key):
    python -X utf8 thi_nghiem_exercises.py

Lưu ý:
    - Câu 1.1 và 2.1 gọi API THẬT → cần key trong .env và có tốn một khoản rất nhỏ.
    - Câu 1.3 và 2.2 chỉ tính toán, KHÔNG gọi API (chạy được kể cả không có key).
"""

from template import (
    call_openai,
    chat_with_system_prompt,
    count_tokens,
    PRICING_PER_1K_TOKENS,
)


def cau_1_1():
    print("\n" + "=" * 70)
    print("CÂU 1.1 — Độ nhạy của temperature (gọi API thật)")
    print("=" * 70)
    prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."
    for temp in (0.0, 0.5, 1.0, 1.5):
        try:
            text, latency = call_openai(prompt, temperature=temp)
            print(f"\n--- temperature = {temp}  ({latency:.2f}s) ---")
            print(text)
        except Exception as e:
            print(f"\n--- temperature = {temp} --- LỖI: {e}")
    print("\n>> Quan sát: temperature càng cao thì 4 câu trả lời càng khác nhau /")
    print(">> sáng tạo hơn hay càng lặp lại/ổn định? Viết nhận xét vào Câu 1.1.")


def cau_2_1():
    print("\n" + "=" * 70)
    print("CÂU 2.1 — Sức mạnh của persona (gọi API thật)")
    print("=" * 70)
    question = "Giải thích blockchain là gì?"
    personas = {
        "Giáo viên tiểu học": "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi.",
        "Chuyên gia tài chính": "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật.",
    }
    for ten, system_prompt in personas.items():
        try:
            text, _ = chat_with_system_prompt(system_prompt, question)
            print(f"\n--- Persona: {ten} ---")
            print(text)
        except Exception as e:
            print(f"\n--- Persona: {ten} --- LỖI: {e}")
    print("\n>> Quan sát: hai câu trả lời khác nhau ra sao về độ dài, từ vựng,")
    print(">> ví dụ? Viết nhận xét vào Câu 2.1.")


def cau_2_2():
    print("\n" + "=" * 70)
    print("CÂU 2.2 — tiktoken vs đếm từ (chỉ tính, KHÔNG gọi API)")
    print("=" * 70)
    doan_van = (
        "Việt Nam là một quốc gia nằm ở khu vực Đông Nam Á, nổi tiếng với nền "
        "văn hóa lâu đời và cảnh quan thiên nhiên tươi đẹp. Từ những thửa ruộng "
        "bậc thang ở vùng núi phía Bắc cho đến các bãi biển cát trắng trải dài ở "
        "miền Trung, đất nước này mang trong mình vẻ đẹp đa dạng. Người dân Việt "
        "Nam thân thiện, cần cù và luôn tự hào về lịch sử hàng nghìn năm."
    )
    so_tu = len(doan_van.split())
    token_that = count_tokens(doan_van, "gpt-4o")
    uoc_luong = so_tu / 0.75
    chenh_lech = (token_that - uoc_luong) / uoc_luong * 100
    print(f"Số từ (đếm theo dấu cách):        {so_tu}")
    print(f"Token thật (tiktoken, gpt-4o):     {token_that}")
    print(f"Ước lượng số_từ / 0.75:            {uoc_luong:.1f}")
    print(f"Chênh lệch:                        {chenh_lech:+.1f}%")
    print("\n>> Viết hai con số + phần trăm chênh lệch này vào Câu 2.2, kèm lý do")
    print(">> tiếng Việt tốn token (dấu thanh, ký tự Unicode nhiều byte).")


def cau_1_3():
    print("\n" + "=" * 70)
    print("CÂU 1.3 — Đánh đổi chi phí (chỉ tính, KHÔNG gọi API)")
    print("=" * 70)
    users, calls_per_user, out_tokens = 10_000, 3, 350
    tong_token = users * calls_per_user * out_tokens          # token output / ngày
    nghin_token = tong_token / 1000
    gia_4o = PRICING_PER_1K_TOKENS["gpt-4o"]["output"]
    gia_mini = PRICING_PER_1K_TOKENS["gpt-4o-mini"]["output"]
    chi_phi_4o = nghin_token * gia_4o
    chi_phi_mini = nghin_token * gia_mini
    print(f"Tổng lời gọi/ngày:          {users*calls_per_user:,}")
    print(f"Tổng token output/ngày:     {tong_token:,}")
    print(f"Chi phí GPT-4o/ngày:        ${chi_phi_4o:,.2f}  (~${chi_phi_4o*30:,.0f}/tháng)")
    print(f"Chi phí GPT-4o-mini/ngày:   ${chi_phi_mini:,.2f}  (~${chi_phi_mini*30:,.0f}/tháng)")
    print(f"GPT-4o đắt hơn mini:        {chi_phi_4o/chi_phi_mini:.1f} lần")
    print("\n>> Viết các con số này vào Câu 1.3, kèm 1 ví dụ nên dùng 4o và 1 ví dụ nên dùng mini.")


if __name__ == "__main__":
    # Hai câu chỉ tính toán — luôn chạy được:
    cau_1_1()
    cau_1_3()
    cau_2_1()
    cau_2_2()

    # Hai câu gọi API thật — bỏ comment 2 dòng dưới khi bạn đã có key trong .env:
    
    

    print("\n" + "=" * 70)
    print("Xong phần TÍNH TOÁN (Câu 1.3, 2.2).")
    print("Muốn chạy Câu 1.1 & 2.1 (gọi API thật): mở file này, bỏ comment 2 dòng")
    print("cuối trong khối __main__ rồi chạy lại.")
    print("=" * 70)
