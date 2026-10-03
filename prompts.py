BILL_READING_PROMPT = """
Read this bill image carefully.

Extract all available bill information.

Return ONLY valid JSON in exactly this format:

{
  "items": [
    {
      "item": "item name",
      "quantity": 1,
      "price": 0,
      "gst": 0,
      "subtotal": 0
    }
  ],
  "total": 0
}

Rules:
- item = product/item name
- quantity = quantity purchased
- price = price per unit if available
- gst = GST amount for that item if shown
- subtotal = amount for that item including GST if shown
- total = final bill total
- Use numbers only for prices and amounts.
- If quantity is not visible, use 1.
- If GST is not shown, use 0.
- Do NOT guess prices.
- Read the values directly from the bill.
"""