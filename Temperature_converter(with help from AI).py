def main():
  print("Hello, Welcome to Tempreature Converter")
  print("1.fahrenheit_to_celsius")
  print("2.celsius_to_fahrenheit")
  print("3.quit")
  
  choice=input("Please Select an Option (1-3)")

  if choice == '1':
    celsius=float(input("Enter temperature in celsius:"))
    print(f"{celsius}c is {celsius_to_fahrenheit(celsius):.2f}c")
  elif choice == '2':
    fahrenheight_to_celsius=float(input("Enter temperature in fahrenheit:"))
    print(f"{fahrenheit} f is {fahrenheit_to_celsius(fahrenheit):.2fc}")
  elif choice =='3':
    print("Goodbye.")
    break
  else:
    print("invalid choice. please select 1,2,or 3")

def fahrenheit_to_celsius(fahr):
  return (fahr-32)*5/9

def celsius_to_fahrenheit(celsius):
  return 9/5*celsius+32
