num = ''                                                                 #กำหนดให้เป็น string ว่าง เพื่อรอรับตัวเลขในtype string
test =[]                                                                 #สร้างเป็นlistว่างเพื่อรอรับตัวเลขจาก num และแปลงมาเป็น list
result = ''                                                              #สร้าง string ว่าง เพื่อแปลงค่ากลับมาเป็น last formed number
count = 0                                                                #เพื่อนับว่าเพิ่มเลขไปแล้วกี่ครั้ง

print('Enter 4 set of integer you like')                                 #แจ้งว่าให้ใส่อะไรบ้าง
while count != 4:                                                        #ให้วนลูปเมื่อยังใส่เลขที่ถูกต้องไม่ครบ 4 ครั้ง
    
    try:                                                                 #ใช้ try เพื่อกันข้อผิดพลาดเวลาใส่ข้อมูลที่ไม่ใช่ integer แล้วโปรแกรมจะหยุดทำงาน
        
        A = input('Enter number.\n')                                     #ใส่ตัวเลขที่ต้องการ
        
        if int(A) < 0:                                                   # เช็คว่าถ้าเลขที่ใส่น้อยกว่า 0 ให้แจ้งว่าต้องใส่มากกว่า 0
            print('Must be higher than 0.\n ')                   
               
        else :                                                           #ถ้าเลขที่ใส่มาเป็น integer ที่ถูกต้อง
            num = num + A                                                #เพิ่มเลขที่ใส่ไปใน string ,อัพเดต num
            count = count + 1                                            #นับว่าใส่ถูกต้องไปแล้วกี่ครั้ง
            print('you have add ',count,'set of number')                 #แจ้งว่าใส่ถูกต้องไปแล้วกี่ครั้ง
            
    except ValueError:                                                   #เมื่อเกิดข้อผิดพลาดให้รันคำสั่งดังต่อไปนี้แทน                                                 
        print('Must be integer.\n')                                      # เมื่อไม่ได้ใส่ข้อมูลที่เป็น integer ให้แจ้งว่าต้องเป็น integer เท่านั้น
                      
for i in num:                                                            #รันทุกตำแหน่งใน num กำหนดให้ตัวแปรคือ i
    test.append(int(i))                                                  #นำตัว i ที่รันได้ไปใส่ใน list ที่ชื่อ test เพื่อให้หาค่า max ได้
    
while len(test) > 0:                                                     #ทำต่อไปจนกว่าจะไม่เหลือเลขให้รัน
    for i in test: 
        if i == max(test):                                               #ถ้ารัน i แล้ว i = ค่าสูงสุดใน list ของ test
            result = result+str(i)                                       #นำค่านั้นไปใส่ใน string ว่างที่ชื่อ result
            test.remove(i)                                               #นำเลขที่รันแล้วออก
        
            
print('The largest formed number is ',result)                            #โชว์ผลลัพธ์        
