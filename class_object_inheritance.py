'''
class는 object를 만드는 틀
class에는 properties랑 method가 정의되어 있다
변수랑 메소드를 사용가능하게 함

__init__ 는 class로 object를 생성할때 반드시 불려지는 함수다. 따라서 properties를 정의하는 용도로 사용

class에서 정의된 모든 함수는 첫번째 인자로 현재 instance를 언급받는다.
꼭 self일 필요는 없으나 반드시 첫번째 인자!!!

.으로 object를 가공
del로 삭제

class는 처음 정의할때 오브젝트처럼()가 필요없다
근데 상속을 받을때의 경우 (부모class)로 가능
상속하면서 __init__를 재정의하면 부모의 __init__를 더이상 상속안하고 overridding 된다
이때 다시 상속받고자 한다면 __init__안에서 부모명.__init__(self, )를 불러오는게 가능하다

super()로 부모명을 안쓰고서 모든 속성을 상속 받을 수 있다.
super().__init() 여기에는 self도 쓰지 않는다
자식만 가지는 properties를 overriding한 생성자메소드에서 추가 가능

'''