#Pria: Berat badan ideal (kilogram) = [tinggi badan (sentimeter) – 100] – [(tinggi badan (sentimeter) – 100) x 10 persen]
#Wanita: Berat badan ideal (kilogram) = [tinggi badan (sentimeter) – 100] – [(tinggi badan (sentimeter) – 100) x 15 persen]

height = float(input("Enter your height(m): "))
weight = float(input("Enter your weight(kg): "))
bmi_men = [(height-100) - (weight-100) * (10/100)]
bmi_women = [(height-100) - (weight-100) * (15/100)]
print(bmi_men)