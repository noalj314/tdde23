from lab5b import *


def test_pixel_constraint():
    """Test the function pixel constraint"""
    check = pixel_constraint(100, 200, 50, 150, 50, 150)
    valid_pixel= ((numpy.uint8(150), numpy.uint8(100), numpy.uint8(100)))
    result = check(valid_pixel)
    assert result == 1, f"Test failed: Expected 1 got {result}"

    invalid_pixel = ((numpy.uint8(255), numpy.uint8(175), numpy.uint8(10))) #Alla värden är utanför constraint
    result = check(invalid_pixel)
    assert result == 0, f"Test failed: Expected 0 got {result}"

    invalid_hue = ((numpy.uint8(50), numpy.uint8(100), numpy.uint8(100)))  # Hue är utanför constraint
    result = check(invalid_hue)
    assert result == 0, f"Test failed: Expected 0 got {result}"

    invalid_saturation = ((numpy.uint8(110), numpy.uint8(10), numpy.uint8(100)))  # saturation är utanför constraint
    result = check(invalid_saturation)
    assert result == 0, f"Test failed: Expected 0 got {result}"

    invalid_value= ((numpy.uint8(110), numpy.uint8(100), numpy.uint8(190)))  # value är utanför constraint
    result = check(invalid_value)
    assert result == 0, f"Test failed: Expected 0 got {result}"

    valid_max = ((numpy.uint8(200), numpy.uint8(150), numpy.uint8(150))) # testa för maxvärden på constrait
    result = check(valid_max)
    assert result == 1, f"Test failed: Expected 1 got {result}"

    valid_min = ((numpy.uint8(100), numpy.uint8(50), numpy.uint8(50)))  # testa för minvärden på constrait
    result = check(valid_min)
    assert result == 1, f"Test failed: Expected 1 got {result}"
test_pixel_constraint()


def test_generator_from_image():
    """Test the function generator from image"""
    some_list = [(1, 2, 3), (2, "a", 10, 80), [10], "a", 4, 5.0]
    index = generator_from_image(some_list)

    # test for various datatypes
    assert index(0) == (1, 2, 3)
    assert index(1) == (2, "a", 10, 80)
    assert index(2) == [10]
    assert index(3) == "a"
    assert index(4) == 4
    assert index(5) == 5.0

    #Test for faulty input
    try:
        wrong = generator_from_image(some_list[10])
        print(f"success for {some_list[10]}: result {wrong}")
    except IndexError as error:
        print(f"Raised the correct error for input out of range exception: {str(error)}")


test_generator_from_image()


def test_combine_images():
    # Test 1, verifiera att funktionen faktiskt returnerar en lista med samma längd som inputlistan och att alla pixel värden är rimliga
    # Motivering det garanterar att vi har en pixel för varje indata pixel så att bilden som ändras blir lika stor som originalbilden
    hsv_list = [(100, 60, 250)] * 20
    condition = pixel_constraint(0, 0, 0, 0, 0, 0)  # irrelevant i detta då vi bara ska checka längden
    output = combine_images(hsv_list, condition, generator1, generator_from_image(hsv_list))
    assert len(output) == len(hsv_list), f"Expected {len(hsv_list)}, got {len(output)}"
    for pixel in output:
        assert pixel[0] >= 0 and pixel[1] >= 0 and pixel[2] >= 0, f"Invalid pixel value {pixel}"

    # Test 2, checka ifall tomma listor hanteras korrekt
    output = combine_images([], condition, generator1, generator_from_image([]))
    assert output == [], f"Expected an empty list, got {output}"

    try:
        combine_images(0,0,0,0)
    except Exception as error:
        print(error)


test_combine_images()


def test_faulty_pixel_constraint():
    """Check if pixel contraint raises exception for faulty indata"""
    different_values = ["HEJ", (1, 2), (1, 2, 3), (numpy.uint8(10), numpy.uint8(10), "då"), 10,
                        20.0]  # checka om den kastar en undantag för hsv_pixel som inte är en tuple
    condition = pixel_constraint(0, 0, 0, 0, 0, 0)

    for i in different_values:
        try:
            result = condition(i)
            print(f"Success for {i}: result {result}")
        except TypeError as error:
            print(f"Raised the correct TypeError for input {i} exception: {str(error)}")


test_faulty_pixel_constraint()
