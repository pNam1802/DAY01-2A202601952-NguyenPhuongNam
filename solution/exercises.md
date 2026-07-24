# K3 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 9h00–13h00
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay mỗi dòng gợi ý (in nghiêng, bắt đầu bằng
dấu `>`) bằng câu trả lời thật của bạn (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Ở temperature 0.0, phản hồi gần như cố định: gọi nhiều lần vẫn ra cùng một
> "sự thật" an toàn, phổ biến (ví dụ về thủ đô hoặc dân số) với cách diễn đạt
> gần như y hệt. Khi tăng lên 0.5 rồi 1.0, câu trả lời đa dạng dần cả về chủ đề
> lẫn từ ngữ nhưng vẫn mạch lạc; đến 1.5 thì đầu ra rất ngẫu nhiên — đôi khi
> sáng tạo bất ngờ nhưng cũng dễ lạc đề, lặp từ hoặc kém chính xác. Quy luật:
> temperature càng cao thì phản hồi càng đa dạng/sáng tạo nhưng càng kém ổn
> định và kém tin cậy.

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Khoảng 0.2–0.3 (thấp). Chatbot hỗ trợ khách hàng cần câu trả lời nhất quán,
> chính xác và dự đoán được — cùng một câu hỏi nên cho cùng một hướng dẫn, và
> tuyệt đối tránh "bịa" thông tin về chính sách hay sản phẩm. Temperature thấp
> hy sinh tính sáng tạo để đổi lấy độ tin cậy và an toàn, đúng thứ mà dịch vụ
> khách hàng cần. Tôi không đặt hẳn 0.0 để câu chữ vẫn tự nhiên, đỡ máy móc.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> Mỗi ngày có 10.000 × 3 = 30.000 lời gọi, tổng 30.000 × 350 = 10.500.000
> token đầu ra (= 10.500 nghìn-token). Chi phí output: GPT-4o = 10.500 × $0.010
> = **$105/ngày** (~$3.150/tháng); GPT-4o-mini = 10.500 × $0.0006 = **$6,30/ngày**
> (~$189/tháng). Tỷ lệ giá là $0.010 / $0.0006 ≈ **16,7 lần** — và tỷ lệ này
> giống hệt ở chiều input ($0.0025 / $0.00015 ≈ 16,7), nên nhìn chung GPT-4o
> đắt hơn mini khoảng **16–17 lần**. GPT-4o xứng đáng với các tác vụ suy luận
> phức tạp, rủi ro cao (phân tích pháp lý/y tế/tài chính, viết code khó) nơi
> một câu trả lời sai tốn kém hơn nhiều lần khoản chênh lệch. Nên dùng mini cho
> tác vụ khối lượng lớn và đơn giản (phân loại, tóm tắt ngắn, trả lời FAQ, gợi
> ý) — nơi tốc độ và chi phí quan trọng hơn độ tinh vi.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> Với persona "giáo viên tiểu học", phản hồi ngắn, câu đơn giản, nhiều phép so
> sánh đời thường (ví dụ blockchain như một cuốn sổ chung mà cả lớp cùng nhìn
> thấy và không ai xóa lén được), gần như không có thuật ngữ. Với persona
> "chuyên gia tài chính", phản hồi dài và sâu hơn, dùng thuật ngữ kỹ thuật (sổ
> cái phân tán, cơ chế đồng thuận, hàm băm mật mã, tính bất biến) và giả định
> người đọc đã có nền tảng. Cùng một câu hỏi nhưng độ dài, từ vựng, độ sâu và
> ví dụ đều thay đổi hẳn. System prompt là "chỉ thị đạo diễn" định hình vai
> trò, giọng điệu và mức độ chuyên môn của model xuyên suốt phản hồi — mà không
> cần sửa câu hỏi của người dùng.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> Với một đoạn ~118 từ tiếng Việt, `count_tokens` (gpt-4o, tokenizer o200k_base)
> đếm **146 token**, còn ước lượng `số_từ / 0.75` cho **157 token** — ước lượng
> CAO hơn thực tế khoảng **7%**. Nhưng con số này phụ thuộc mạnh vào tokenizer:
> nếu dùng tokenizer đời cũ cl100k_base (gpt-4 / gpt-3.5), cùng kiểu văn bản
> tiếng Việt tốn tới ~2,2 token/từ, so với ~1,3 token/từ của tiếng Anh — tức
> gấp khoảng 1,7 lần. Tiếng Việt thường tốn token hơn tiếng Anh cùng độ dài vì:
> (1) dấu thanh và các ký tự có dấu (ă, â, đ, ê, ô, ơ, ư + 5 dấu) là ký tự
> Unicode nhiều byte, mà tokenizer huấn luyện chủ yếu trên tiếng Anh nên phải
> cắt chúng thành nhiều mảnh nhỏ; (2) tiếng Việt xuất hiện ít trong dữ liệu
> huấn luyện tokenizer nên ít "từ nguyên khối" được gộp sẵn. Tokenizer o200k
> mới của gpt-4o đa ngữ hơn nên đã thu hẹp đáng kể khoảng cách này.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất khi phản hồi dài và có người dùng đang chờ trực
> tiếp — chatbot, trợ lý viết, các câu giải thích dài. Hiển thị từng token giúp
> giảm mạnh "thời gian tới chữ đầu tiên": người dùng thấy hệ thống đang chạy và
> bắt đầu đọc ngay, nên cảm giác nhanh hơn hẳn dù tổng thời gian sinh text
> không đổi. Ngược lại, non-streaming phù hợp hơn khi ta cần trọn vẹn kết quả
> trước khi xử lý tiếp: gọi API trả JSON để parse, tác vụ nền/batch không có ai
> ngồi xem, hoặc khi cần hậu xử lý — kiểm duyệt, xác thực, định dạng lại — cả
> câu trả lời trước khi hiển thị. Streaming cũng làm việc xử lý lỗi giữa chừng
> phức tạp hơn, nên không phải lúc nào cũng đáng dùng.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Khi API đang quá tải, việc retry với delay cố định ngắn chỉ đổ thêm tải vào
> một server vốn đã nghẽn, kéo dài tình trạng quá tải. Exponential backoff tăng
> gấp đôi thời gian chờ sau mỗi lần thất bại (0.1 → 0.2 → 0.4...), vừa cho server
> thời gian hồi phục vừa tự động giãn tần suất gọi khi lỗi kéo dài. Nếu hàng
> nghìn client cùng retry với đúng một delay cố định giống nhau, chúng sẽ "đồng
> pha": cùng dội request vào đúng những mốc thời gian trùng nhau, tạo ra các
> đợt sóng tải đồng loạt (thundering herd) khiến server càng khó gượng dậy.
> Trong thực tế người ta còn thêm "jitter" — một lượng nhiễu ngẫu nhiên vào mỗi
> delay — để phá vỡ sự đồng pha đó và trải đều các lần retry.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Persona: **"Bạn là trợ giảng thân thiện của khóa AI, trả lời ngắn gọn bằng
> tiếng Việt."** Hai lựa chọn từ ngữ quan trọng: (1) "trả lời ngắn gọn" để kiểm
> soát độ dài đầu ra — vừa tiết kiệm token/chi phí, vừa hợp với giao diện dòng
> lệnh (câu quá dài rất khó đọc trên terminal); (2) "bằng tiếng Việt" để chỉ
> định ngôn ngữ, tránh việc model mặc định trả lời tiếng Anh khi câu hỏi có lẫn
> thuật ngữ tiếng Anh. Cụm "trợ giảng thân thiện" đặt vai trò và giọng điệu gần
> gũi, khuyến khích người học hỏi tiếp thay vì trả lời khô khan như tra cứu.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Hạn chế lớn nhất là history chỉ giữ 3 lượt gần nhất (`history[-6:]`), nên trợ
> lý "quên" thông tin nói ở đầu phiên — ví dụ tên người dùng hay bối cảnh đặt
> ra từ lượt đầu tiên. Cải thiện: thay vì cắt cứng, dùng "bộ nhớ tóm tắt hội
> thoại" (conversation summary memory) — tóm tắt các lượt cũ thành vài câu rồi
> đưa vào ngữ cảnh, đồng thời giữ nguyên văn vài lượt gần nhất. Cách triển khai:
> khi history vượt quá N message, gọi thêm một lượt API yêu cầu model tóm tắt
> các lượt cũ thành 2–3 câu, lưu vào biến `summary`, ghép bản tóm tắt đó vào
> messages dưới dạng một system message ("Tóm tắt hội thoại trước: ..."), rồi
> chỉ giữ K lượt mới nhất ở dạng nguyên văn. Nhờ vậy trợ lý giữ được bối cảnh
> dài mà token đầu vào không phình vô hạn theo thời gian trò chuyện.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/` và zip theo hướng dẫn README
