# Case-study # 2: Monopolist optimization
# Developers: Fedotova M., Ogorodnikova M., Shepeleva U.
#

import ru_local as ru

def main():
    '''
    Main function.
    :return: None
    '''

    demand_function = input(ru.DEMAND_FUNCTION)
    gross_cost_function = input(ru.GROSS_COST_FUNCTION)
    demand_coeffs = demand_function.replace('P = ', '').replace(' ', '').split('-')
    a = int(demand_coeffs[0])
    b = int(demand_coeffs[1].split('*')[0])
    gross_coeffs = gross_cost_function.replace('TC =', '').replace(' ', '').split('+')
    c = int(gross_coeffs[0].split('*')[0])
    d = int(gross_coeffs[1])
    q = 2

    # 1
    TR = (a - b * q) * q
    TR_prev = (a - b * (q - 1)) * (q - 1)
    MR = TR - TR_prev
    TC = c * q + d
    C_prev = c * (q - 1) + d
    MC = TC - C_prev

    # 2
    optimal_volume = None
    if MR == MC:
        optimal_volume = q
    else:
        optimal_volume = q

    # 3
    P = a - b * optimal_volume

    # 4
    TR = P * optimal_volume
    TC_new = c * optimal_volume + d
    profit = TR - TC_new

    # 5
    optimal_volume_competition = MC

    # 6
    price_competition = MC

    print(f'{ru.MARGINAL_REVENUE}{MR}, {ru.MARGINAL_COSTS}{MC}')
    print(f'{ru.OPTIMAL_VOLUME}{optimal_volume}')
    print(f'{ru.PRICE}{P}')
    print(f'{ru.PROFIT}{profit}')
    print(f'{ru.OPTIMAL_VOLUME_COMPETITION}{optimal_volume_competition}')
    print(f'{ru.PRICE_COMPETITION}{price_competition}')


if __name__ == '__main__':
    main()
