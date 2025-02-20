input = input ("Enter the feet and inches : ")

def convert (input):
    parts = input.split(" ")
    feet = float (parts[0])
    inches = float (parts[1])

    meter = feet * 0.3048 + inches * 0.0254

    return meter

print (convert(input))