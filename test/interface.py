import sys
import os
#from ModularHydroponics.ModularHydroponics
import menu

'''
시간나면 Inquirer 써서 해볼수도
def handleoption(cmd, men):
    if cmd.isdecimal() and int(cmd) > 0:
        try:
            if isinstance(men.subMenuObj[int(cmd)-1], menu.ExecOption) or isinstance(men.subMenuObj[int(cmd)-1], menu.ToggleOption):
                men.subMenuObj[int(cmd) - 1].run()
                men.run()
                return men
            else:
                men.subMenuObj[int(cmd) - 1].run()
                return men.subMenuObj[int(cmd) - 1]
        except:
            print('invalid submenu')
            return men
    elif cmd.isdecimal() and int(cmd) == 0:
        if not men.is_top():
            print('back to prevmenu')
            men.prevMenu.run()
            return men.prevMenu
        else:
            while True:
                ans = input('Quit program? Y/N>> ')
                for words in ['N', 'n', 'Y', 'y']:
                    if ans in words:
                        out = True
                        break
                    else:
                        out = False
                if out:
                    break
            if (ans in 'N') or (ans in 'n'):
                men.run()
                return men
            else:
                sys.exit(1)
    else:
        return men
'''
def cmd_line(menusetup, **kwargs):
    currentmenu = menusetup(**kwargs)
    currentmenu.run()
    while True:
        os.system('cls')
        cmd = input('\nSelect> ')
        try:
            currentmenu = handleoption(cmd, currentmenu)

        except KeyboardInterrupt:
            sys.exit(1)
            pass


def handleoption(cmd, men):
    if cmd.isdecimal() and int(cmd) > 0:
        try:
            if isinstance(men.subMenuObj[int(cmd)-1], menu.ExecOption or menu.ExecOptionQ or menu.ToggleOption):
                men.subMenuObj[int(cmd) - 1].run()
                men.run()
                return men
            else:
                men.subMenuObj[int(cmd) - 1].run()
                return men.subMenuObj[int(cmd) - 1]
        except:
            print('invalid submenu')
            return men

    elif cmd.isdecimal() and int(cmd) == 0:
        if not men.is_top():
            print('back to prevmenu')
            men.prevMenu.run()
            return men.prevMenu
        else:   #men.is_top == True
            while True:
                men.display.lcd_clear()
                men.lcd_write(men.display, 'Quit program? Y/N>> ', 1)
                ans = input('Quit program? Y/N>> ')
                for words in ['N', 'n', 'Y', 'y']:
                    if ans in words:
                        out = True
                        break
                    else:
                        out = False
                if out:
                    break

            if (ans in 'N') or (ans in 'n'):
                men.run()
                return men
            else:
                men.display.lcd_clear()
                men.lcd_write(men.display, 'System off', 1)
                sys.exit(1)

    else:
        return men
