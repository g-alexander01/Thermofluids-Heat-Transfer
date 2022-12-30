##
# Key info:
# - Heat transfer occours through 3 mechanisms - conduction, convection, and radiation
# - Main interest lies in the external walls, windows, roof and ground floor (contact with outside world)
# - Therfore internal walls and floors will not be considered in calculation as house temp is homogeneous
# #


# function that returns heat flux value for indefintley layered composite wall
def heat_loss(h_inside, h_outside, area, layers):

    # temperatures in kelvin
    in_temp = 25 + 273.15
    out_temp = 10.8 + 273.15

    # sum of li / ki
    sum = 0

    # looping through array of layer data to calc li / ki
    for i in range(len(layers)):

        depth = layers[i][0]
        k = layers[i][1]
        sum += depth / k

    # calculating heat flux value
    q = (in_temp - out_temp) / ((1 / h_inside) + sum + (1 / h_outside))
    print(f"Heat flux: {q}")

    # scaling flux by area and returning value
    print(round(area * q, 2))
    print("\n")
    return 



# arguments given in form (h_i, h_o, area, layers[])
# a.k.a (inside heat convection transfer coef, outside heat transfer coef, surface area, [[layer depth, thermal cond.], ...])

print("Walls:")
heat_loss(3, 14, 202.44, [[0.016, 0.26], [0.22, 0.84]])

print("Window:")
heat_loss(5.6, 16, 8.69, [[0.004, 1.05]])

print("Door:")
heat_loss(2.32, 10, 3.56, [[0.1, 0.1213]])

# following calculations use updated temperature values as described
# takes attic temp (colder than house) and ground temp (warmer than outside) into account

print("Ceiling:")
heat_loss(3, 3, 65.36, [[0.03, 0.26], [0.008, 0.14], [0.15, 0.025], [0.03, 0.14]])       # inside temp = 25, outside = 15

print("Roof:")
heat_loss(4.3, 18.1, 110.66, [[0.006, 0.84]])       # inside temp = 15, outside = 10

print("Floor")
heat_loss(3, 24, 65.36, [[0.03, 0.14], [0.5, 0.025], [0.1, 1.4]])       # inside temp = 25, outside ground temp = 10.8

# -------------------------

# calculation of heat flux and heat loss values after intervention
print("Walls 2:")
heat_loss(3, 0.157, 202.44, [[0.025, 0.045], [0.2, 0.08]])

print("Window 2:")
heat_loss(5.6, 1.3, 8.69, [[0.006, 1.8], [0.016, 0.016], [0.006, 1.8]])

# door is not recalculated as no material changes were implemented


# changing temp value calculations
# attic temps changed after intervention - warmer as house more insulated

print("Roof 2:")
heat_loss(3, 18.1, 110.66, [[0.03, 0.14], [0.4, 0.039], [0.003, 0.022], [0.006, 0.84]])       # inside temp = 18, outside = 10

print("Ceiling 2:")
heat_loss(3, 3, 65.36, [[0.03, 0.045], [0.008, 0.14], [0.2, 0.035]])      # inside temp = 25, outside = 18

print("Floor 2:")
heat_loss(3, 24, 65.36, [[0.03, 0.14], [0.3, 0.039], [0.003, 0.022], [0.4, 0.025], [0.1, 1.4]])       # inside temp = 25, outside ground temp = 10.8