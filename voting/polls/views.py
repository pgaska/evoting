from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from .ecurve.elliptic import EllipticCurve
from .ecurve.elgamal import Elgamal
from .ecurve.point import Point

class Curve(object):
   def __init__(self):
       self.p=8884933102832021670310856601112383279507496491807071433260928721853918699951
       self.n=8884933102832021670310856601112383279454437918059397120004264665392731659049
       self.a4=2481513316835306518496091950488867366805208929993787063131352719741796616329
       self.a6=4387305958586347890529260320831286139799795892409507048422786783411496715073
       self.r4=5473953786136330929505372885864126123958065998198197694258492204115618878079
       self.r6=5831273952509092555776116225688691072512584265972424782073602066621365105518
       self.gx=7638166354848741333090176068286311479365713946232310129943505521094105356372
       self.gy=762687367051975977761089912701686274060655281117983501949286086861823169994
       self.r=8094458595770206542003150089514239385761983350496862878239630488323200271273


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions':questions})

def list(request):
    return render(request, 'polls/list.html')

def receipt(request):
    return render(request, 'polls/receipt.html')

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question':question})

def choose_digit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    for choice in question.choice_set.all():
        print(choice.id)
        curve = Curve()
        elgamal = Elgamal(curve)
        (publickey, privatekey) = elgamal.keygen()
        (c1, c2) = elgamal.encrypt(publickey, choice.id)
        cipher = str(c1)
        cipher += str(c2.x)
        cipher += str(c2.y)

        Choice.objects.filter(pk=choice.id).update(public_key_x_0=publickey.x, public_key_y_0=publickey.y, private_key_0=privatekey, ciphered_answer_0=cipher)
        curve = Curve()
        elgamal = Elgamal(curve)
        (publickey, privatekey) = elgamal.keygen()
        (c1, c2) = elgamal.encrypt(publickey, choice.id)
        cipher = str(c1)
        cipher += str(c2.x)
        cipher += str(c2.y)
        Choice.objects.filter(pk=choice.id).update(public_key_x_1=publickey.x, public_key_y_1=publickey.y, private_key_1=privatekey, ciphered_answer_1=cipher)


    return render(request, 'polls/choose_digit.html', {'question':question})