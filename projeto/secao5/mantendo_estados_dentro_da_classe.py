# Mantendo estados dentro da classe.

class Camera:
    def __init__(self, name: str, filming=False):
        self.name = name
        self.filming = filming
    
    def on(self):
        if self.filming:
            print("Already filming")
            return
        
        self.filming = True
        return
    
    def off(self):
        if self.filming is False:
            print("It's already turned off")
            return
        
        self.filming = False
        return
    
    def photograph(self):
        if self.filming:
            print("You can't take pictures while filming")
            return
        print("Photograph...")
        return
    
    def stop_filming(self):
        self.filming = False
        return
cam = Camera("DSLR")
print(cam.name)
print(cam.filming)

cam.on()
print(cam.filming)

cam.photograph()
cam.stop_filming()
cam.photograph()