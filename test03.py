#คำนวณหาราคาขายสินค้า โดยรับซื้อสินค้า และราคาสินค้า(ต้นทุน) ทางแป้นพิมพ์
#แล้วคำนวณหาราคาสินค้า โดยราคาขายสินค้าจะคิดเพิ่มจากราคา(ต้นทุน) ร้อนละ 10
#สูตร ราคาขายสินค้า = ราคาสินค้า (ต้นทุน) - (ราคาสินค้า(ต้นทุน) * 10 / 100)

#feature ในการรับสินค้า การคำนวณ และการแสดงผลแยกจากกัน
#ดังนั้นอย่างน้อยมี 3 ฟังก์ชัน

def inputData( ) :
    product_name = input('ป้อนชื่อสินค้า')
    pr