import math

def main():
    radius = 6.83
    height = 10.16
    can_volume = volume(radius, height)
    can_surface_a = surface_area(radius, height)
    s_final_efficiency = storage_efficiency(can_volume, can_surface_a)

    print(f"result is: {s_final_efficiency: .1f}")

# function to calculate the volume of the can


def volume(radius, height):
    cylinder_volume = math.pi * (radius ** 2) * height
    cylinder_volume = round(cylinder_volume, 2)
    return cylinder_volume
    # print(cylinder_volume)

# function to calculate the surface area


def surface_area(radius, height):
    surface_a_formula = (2 * math.pi) * (radius) * (radius + height)
    surface_a_formula = round(surface_a_formula, 2)
    return surface_a_formula

# function to calculate the storage efficiency


def storage_efficiency(volume, surface_area):
    s_efficiency_formula = volume / surface_area
    return s_efficiency_formula


# call the main function
main()
