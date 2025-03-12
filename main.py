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
    TC_prev = c * (q - 1) + d
    MC = TC - TC_prev

    # 2
    Q = MR - MC
    
    # 3
    P = a - b * Q

    # 4
    TR = P * Q
    TC_new = c * Q + d
    profit = TR - TC_new

    # 5
    optimal_volume_competition = P - MC
    
    print(f'{ru.MARGINAL_REVENUE}{MR}, {ru.MARGINAL_COSTS}{MC}')
    print(f'{ru.OPTIMAL_VOLUME}{Q}')
    print(f'{ru.PRICE}{P}')
    print(f'{ru.PROFIT}{profit}')
    print(f'{ru.OPTIMAL_VOLUME_COMPETITION}{optimal_volume_competition}')


if __name__ == '__main__':
    main()
