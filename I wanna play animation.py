Frame1 = """






     OOOO
    OOOOOO
     OOOO


"""
Frame2 = """



                 OOOOO
               OOOOOOOOO
               OOOOOOOOO
     OOOO        OOOOO
    OOOOOO
     OOOO


"""
Frame3 = """
                                OOOOO0OO
                              OOOOOOOOOOOO
                             OOOOOOOOOOOOOO
                 OOOOO        OOOOOOOOOOOO
               OOOOOOOOO        OOOOO0OO
               OOOOOOOOO
     OOOO        OOOOO
    OOOOOO
     OOOO


"""
Frame4 = """
                                OOOOO0OO              OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                              OOOOOOOOOOOO          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                             OOOOOOOOOOOOOO       OOOO         MMMMDDDDDD                        OOOO
                 OOOOO        OOOOOOOOOOOO       OOOO          MMMMDDDDDDD  SSS  U  U SSS        OOOOO
               OOOOOOOOO        OOOOO0OO          OOOO         MMMMDDDDDDD  S    U  U S          OOO
               OOOOOOOOO                          OOOO         MMMMMMMMM    SSS  U  U SSS         OOOO
     OOOO        OOOOO                           OOOO          MMMM  MMM      S  U  U   S         OOOO
    OOOOOO                                       OOOO          MMMM   MM    SSS   UUU SSS        OOOO
     OOOO                                         OOOO                                          OOOO
                                                    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                                      OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
"""








X = 0
while True:
    X += 1
    if X % 30000000 == 1:
        print(Frame1)
    if X % 30000000 == 10000001:
        print(Frame2)
    if X % 30000000 == 20000001:
        print(Frame3)
    #if X % 50000000 == 30000001:
        #print(Frame4)

