class Methods:
    def instace_method(self):
        return f"called instance method {self}"
    @classmethod
    def class_method(cls):
        return f"called class method {cls}"
    @staticmethod
    def static_method():
        return f"called static method"

obj = Methods()
print(obj.instace_method())

print(Methods.class_method())
print(Methods.static_method())