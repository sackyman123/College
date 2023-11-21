#!/usr/bin/env python3

class Student():
    def set_attributes(self, sid, name, modules):
        self.name = name
        self.sid = sid
        self.modlist = modules
    def print_attributes(self):
        #make modlist a string
        modlist = ""
        if len(self.modlist) == 1:
            modlist = self.modlist[0]
        else:
            for o in self.modlist:
                if o != self.modlist[-1]:
                    modlist += o + ", "
                else:
                    modlist += o
        print(f'ID: {self.sid}\nName: {self.name}\nModules: {modlist}')
    def add_module(self, module):
        self.modlist.append(module)
    def del_module(self, module):
        if module in self.modlist:
            self.modlist.pop(self.modlist.index(module))
        else:
            pass
