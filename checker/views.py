# from datetime import date
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from .forms import *

# # Create your views here.

main_dict = {
    "12":{"Good":"Attractive.Husband Wife Relation Strong Karta Hai.Spouse Care Karta Wala Hota Hai.Financial Stability.Money Saving Person.Good For Businessman"},
    "13":{"Good":"Money Number.Makes Person Professional.Helpful.Good Education.Popular And Respectful.Good For Advisor Job"},
    "31":{"Good":"Money Number.Makes Person Professional.Helpful.Good Education.Popular And Respectful.Good For Advisor Job"},
    "14":{"Negative": "Money Loss,Legal Notice,Health Issue,Debt, Detachment With Relatives,Weak immune System And Bones"},
    "41":{"Negative": "Money Loss,Legal Notice,Health Issue,Debt, Detachment With Relatives,Weak immune System And Bones"},
    "15":{"Good":"Good For Childrens,For Marriage Purpose,This Number Makes Father Popular"},
    "51":{"Good":"Good For Childrens,For Marriage Purpose,This Number Makes Father Popular"},
    "16":{"Negative":"Spouse Health Issue,Relationship Issue,Financial Loss,Less Income Source,Skin and UTI Problem"},
    "61":{"Negative":"Spouse Health Issue,Relationship Issue,Financial Loss,Less Income Source,Skin and UTI Problem"},
    "17":{"Neutral":"Govt. Job Or Good Position In MNC,Chances Of Two Marriage,More Profit from Lying,Never Stop Because Of Money,If Multiple 7 In Grid Then Don't Take This Combination,If 2,5,6 is Missing in Grid Then Don't Take This Combination"},
    "71":{"Neutral":"Govt. Job Or Good Position In MNC,Chances Of Two Marriage,More Profit from Lying,Never Stop Because Of Money,If Multiple 7 In Grid Then Don't Take This Combination,If 2,5,6 is Missing in Grid Then Don't Take This Combination"},
    "18":{"Negative":"Father-Son Relationship Issue,Spouse Health Issue,Frequently Changes In Job,Government Related Issue,Long Health Issue"},
    "81":{"Negative":"Father-Son Relationship Issue,Spouse Health Issue,Frequently Changes In Job,Government Related Issue,Long Health Issue"},
    "19":{"Good":" Freedom Lover,Gives Height in Life,Whatever Wants' Can Earn,Professional, Leader,Rasukhdar"},
    "91":{"Good":" Freedom Lover,Gives Height in Life,Whatever Wants' Can Earn,Professional, Leader,Rasukhdar"},
    "21":{"Neutral":"Unwanted Expenses,Attractive Personality,Attractive Face,Can't Save Money"},
    "23":{"neutral":" Parenting Happiness Delay,Lots of Enemy but No one can Harm,Extra Marital Affairs,Love to Watch Outside the House,Egoistic"},
    "32":{"neutral":" Parenting Happiness Delay,Lots of Enemy but No one can Harm,Extra Marital Affairs,Love to Watch Outside the House,Egoistic"},
    "24":{"Neutral":"Keep Patience to Achieve Something,Negative Thought,Depression,Moody,Destructive Thinking"},
    "42":{"Neutral":"Keep Patience to Achieve Something,Negative Thought,Depression,Moody,Destructive Thinking"},
    "25":{"Good":" Clever,Achieve Success in Occult and Medical,Do Logo Ke Jhagde Suljhane Wala,Spiritual Business,Success Through Air Travel"},
    "52":{"Good":" Clever,Achieve Success in Occult and Medical,Do Logo Ke Jhagde Suljhane Wala,Spiritual Business,Success Through Air Travel"},
    "26":{"Negative":" Interruption in Study,Relationship issue Between Saas And Bahu,Attraction Towards Opposite Sex,Chances of less Sperm count or Diabetes,Useless Expenses,Debt"},
    "62":{"Negative":" Interruption in Study,Relationship issue Between Saas And Bahu,Attraction Towards Opposite Sex,Chances of less Sperm count or Diabetes,Useless Expenses,Debt"},
    "27":{"Negative":"UTI Infection, Joint Pain, Arthritis Related Issue,Money Never Stop,Medical Expenses,Negative Thinking,Good Intuition"},
    "72":{"Negative":"UTI Infection, Joint Pain, Arthritis Related Issue,Money Never Stop,Medical Expenses,Negative Thinking,Good Intuition"},
    "28":{"Negative":"Two Marriage,Medical Expenses,Earns Good But Lots of Useless Expenses,Avoid Bad Company,Wife/Mother Health Issue,Vish Yog"},
    "82":{"Negative":"Two Marriage,Medical Expenses,Earns Good But Lots of Useless Expenses,Avoid Bad Company,Wife/Mother Health Issue,Vish Yog"},
    "29":{"Good":"Financial Stability,Egoistic,Person Can Earn Own Money,Enjoy Life Happily,Laxmi Yog"},
    "92":{"Good":"Financial Stability,Egoistic,Person Can Earn Own Money,Enjoy Life Happily,Laxmi Yog"},
    "34":{"Negative":"Breathing Related Issue,,Leg Pain Or Shivering,Criminal Minded,Gets Cheated Or Cheat Others"},
    "43":{"Negative":"Breathing Related Issue,,Leg Pain Or Shivering,Criminal Minded,Gets Cheated Or Cheat Others"},
    "35":{"Neutral":"Fear of Father/Society Hence Successful,Good Financial Condition,Liquid Money Issue,Get Success Away From Home,Good For Commission Business"},
    "53":{"Neutral":"Fear of Father/Society Hence Successful,Good Financial Condition,Liquid Money Issue,Get Success Away From Home,Good For Commission Business"},
    "36":{"Neutral":"Good Knowledge but Confidence Issue,Multi Talented,Barrier in Study,Principal Oriented Person"},
    "63":{"Neutral":"Good Knowledge but Confidence Issue,Multi Talented,Barrier in Study,Principal Oriented Person"},
    "73":{"Good": '''everyone will support.good knowledge.complete personality.success in every field'''},
    "37":{"Good": "everyone will support\.good knowledge\n complete personality\n success in every field"},
    "38":{"Good":"Get Benefit From Real Estate, Counseling And Sales Related Work,Mediator Between Two Parties, Peace Maker"},
    "83":{"Good":"Get Benefit From Real Estate, Counseling And Sales Related Work,Mediator Between Two Parties, Peace Maker"},
    "39":{"Neutral":"Like to Show Off,Good For Reserve Person,Duality in Nature,Ziddi Person(Stubborn),Good For Occult, Doctor, Teacher and Healer"},
    "93":{"Neutral":"Like to Show Off,Good For Reserve Person,Duality in Nature,Ziddi Person(Stubborn),Good For Occult, Doctor, Teacher and Healer"},
    "45":{"Negative":"Bandhan Yog,Lots of Medical Expenses,Court Case and Legal Issue,Life is full of Restriction,Losses"},
    "54":{"Negative":"Bandhan Yog,Lots of Medical Expenses,Court Case and Legal Issue,Life is full of Restriction,Losses"},
    "46":{"Negative":"Not Good For Student,Inter Cast Marriage,Skin And UTI Infection,Extra Marital Affair"},
    "64":{"Negative":"Not Good For Student,Inter Cast Marriage,Skin And UTI Infection,Extra Marital Affair"},
    "47":{"Good":" Honest,Brilliant,Rahu-Ketu Combo,Good For Occult,Quality To Being Honest"},
    "74":{"Good":" Honest,Brilliant,Rahu-Ketu Combo,Good For Occult,Quality To Being Honest"},
    "48":{"Negative":" Diabetes, BP, Blood Related Disease,Incurable/Chronic Disease,Deficiency Of Sexual Pleasure,Unaccepted Accident,Court Case"},
    "84":{"Negative":" Diabetes, BP, Blood Related Disease,Incurable/Chronic Disease,Deficiency Of Sexual Pleasure,Unaccepted Accident,Court Case"},
    "49":{"Neutral":"Criminal Minded,Hard Worker,Uniform Work(Police/Sports/Army),Court Case,Jugadu Person"},
    "94":{"Neutral":"Criminal Minded,Hard Worker,Uniform Work(Police/Sports/Army),Court Case,Jugadu Person"},
    "56":{"Neutral":"Hesitate To Ask For Own Money,Business Minded,Cheating In Love"},
    "65":{"Neutral":"Hesitate To Ask For Own Money,Business Minded,Cheating In Love"},
    "57":{"Good":"Good Advisor,Public Relation,Good Expressive Person,Good For Astrologer, Speaker, Writer,Lots Of Persons Comes For advice,Good For Occult"},
    "75":{"Good":"Good Advisor,Public Relation,Good Expressive Person,Good For Astrologer, Speaker, Writer,Lots Of Persons Comes For advice,Good For Occult"},
    "58":{"Neutral":" Money Stuck,Person Work Related Money And Finance,Calculative Mind,Property Loss/ Financial Loss,Always Talk About Lakh And Crores"},
    "85":{"Neutral":" Money Stuck,Person Work Related Money And Finance,Calculative Mind,Property Loss/ Financial Loss,Always Talk About Lakh And Crores"},
    "59":{"Neutral":"Destroy Relation Through Straight Forward, Sharp Minded, Science/ Commerce Stream Person, If CN/DN is 4 or 9 then don't take this"},
    "95":{"Neutral":"Destroy Relation Through Straight Forward, Sharp Minded, Science/ Commerce Stream Person, If CN/DN is 4 or 9 then don't take this"},
    "67":{"Neutral":"Dispute In Husband And Wife Relationship,Chances Of Love Marriage,Spouse Health Issue,Music Lover,Baccho Se Khushi Nahi Milti Hai"},
    "76":{"Neutral":"Dispute In Husband And Wife Relationship,Chances Of Love Marriage,Spouse Health Issue,Music Lover,Baccho Se Khushi Nahi Milti Hai"},
    "68":{"Negative":"Eyes Problem,Health Related Problems (Issue in Any Organ of Body),Operation Chances (Head to Stomach),Good For Surgeon, Doctor And Hospital Job,If multiple 1 in DOB then highly chances native phases struggle from the long time."},
    "86":{"Negative":"Eyes Problem,Health Related Problems (Issue in Any Organ of Body),Operation Chances (Head to Stomach),Good For Surgeon, Doctor And Hospital Job,If multiple 1 in DOB then highly chances native phases struggle from the long time."},
    "69":{"good":"Good Planner(Event Management),Good Management Skill,Team Work With Opp. Sex will be Fruitful,Chances Of Love Marriage"},
    "96":{"good":"Good Planner(Event Management),Good Management Skill,Team Work With Opp. Sex will be Fruitful,Chances Of Love Marriage"},
    "78":{"Neutral":" Idealistic,Good For Healer/Doctor/Reiki,Power To Solve anything By Own,If Multiple 7 Then Don't Take (Relationship Issue)"},
    "87":{"Neutral":" Idealistic,Good For Healer/Doctor/Reiki,Power To Solve anything By Own,If Multiple 7 Then Don't Take (Relationship Issue)"},
    "79":{"Neutral":"Success after separation from Father,Sometimes Ups And Down in Job/Business,Opposite Gender Attraction"},
    "97":{"Neutral":"Success after separation from Father,Sometimes Ups And Down in Job/Business,Opposite Gender Attraction"},
    "89":{"Neutral":"Aggressive,Argumentive,Works with Principal,Chronic Issue in Later Life,High BP ,Sugar,Good For Business Person"},
    "98":{"Neutral":"Aggressive,Argumentive,Works with Principal,Chronic Issue in Later Life,High BP ,Sugar,Good For Business Person"},
    "11":{"Good":"Communication Authentic,Innovative,Able To Convey the Id,Confidence"},
    "111":{"Neutral":"Ego,Attitude,Communication"},
    "22":{"Neutral":"Mood Swing,Creative, Emotional,Take Care Of Family"},
    "222":{"Negative":"  High Mood Swing, Depression,Too Much Emotional,B P Low"},
    "33":{"Good":" Education, Story Telling,Good Creator, Learning Person"},
    "333":{"Neutral":"Hungry For Knowledge,Over thinking,Curious To Learn New Things,Trust Issu, Deep Thinking"},
    "44":{"Negative": "Legal Issue, Debt,Infliction Pain, Gastric Issue"},
    "444":{"Negative":" Struggle,Headache,Joint Pai, Health Issue"},
    "55":{"Good":"Communication,Adventure,Tendency To create New Experience"},
    "555":{"Neutral":"Lazy ,Always Tired Communication and Money can Increase"},     
    "66":{"Good":"Luxury Lover,Travelling, Lives Like a kin, Loves To Maintain Kids"},
    "666":{"Neutral":" Luxury Lover,Likes Travelling, Money Flow, Glamour, Relationship With Multiple People "},
    "77":{"Neutral":" Mood Swing,Spiritual, Knowledgeable, Learning"},
    "777":{"Negative":" Mood Swing,Internal Disturbance,Spirituality, Over Thinking,Major Relationship Issue,Health Issue"},
    "88":{"Neutral":" Delay,Disturbance, Obstacle, Loan "},
    "888":{"Negative":"Labouring, Delay, Disturbance,Obstacles,Hard Working"},
    "99":{"Neutral":"Humanitarian,Spiritual, Ego,Rough And Tough,Good Business Sense"},   
    "999":{"Neutral":"Debt, Anger, Blood Relation Issue, Good For Gym/Sports Club/Aggressive Work, Skin Color"},
    "00":{"Neutral combination but not recommenfded"},
    "000":{"Negative":"Financial Crunche, Set back Again And Agai, If Multiple Zero, Always Back to Zero"},
           


}
# @login_required
# def index(request):
#     if not request.user.has_access:
#         return render(request, 'access_denied.html')
#     context = {}

#     if request.method == "POST":
#         phone_no = request.POST.get("phone_number", "").strip()
#         if len(phone_no) != 10 or not phone_no.isdigit():
#             context["error"] = "Please enter a valid 10-digit phone number."
#         else:
#             sum_of_digits = sum(int(d) for d in phone_no)
#             while sum_of_digits >= 10:
#                 sum_of_digits = sum(int(d) for d in str(sum_of_digits))

#             clean_no = phone_no.replace("0", "")
#             percent = 90
#             combinations_dict = {}

#             # # 2-digit combinations (mandatory)
#             # for i in range(len(clean_no) - 1, 0, -1):
#             #     pair = clean_no[i - 1:i + 1]
#             #     if pair in main_dict:
#             #         combinations_dict[percent] = f"{pair} - {main_dict[pair]}"
#             #     else:
#             #         combinations_dict[percent] = f"{pair} - good"
#             #     percent -= 10

#             # # 3-digit combinations (optional)
#             # for i in range(len(clean_no) - 2):
#             #     triplet = clean_no[i:i + 3]
#             #     if triplet in main_dict:
#             #         combinations_dict[f"special ({triplet})"] = main_dict[triplet]

#             # 2-digit combinations (mandatory)
#             # for i in range(len(clean_no) - 1, 0, -1):
#             #     pair = clean_no[i - 1:i + 1]
#             #     if pair in main_dict:
#             #         tag = list(main_dict[pair].keys())[0]
#             #         message = main_dict[pair][tag]
#             #         combinations_dict[percent] = {"tag": tag, "msg": f"{pair} - {message}"}
#             #     else:
#             #         combinations_dict[percent] = {"tag": "Good", "msg": f"{pair} - good"}
#             #     percent -= 10

#             # # 3-digit combinations (optional)
#             # for i in range(len(clean_no) - 2):
#             #     triplet = clean_no[i:i + 3]
#             #     if triplet in main_dict:
#             #         tag = list(main_dict[triplet].keys())[0]
#             #         message = main_dict[triplet][tag]
#             #         combinations_dict[f"special ({triplet})"] = {"tag": tag, "msg": f"{triplet} - {message}"}

#             # Inside views.py
#             for i in range(len(clean_no) - 1, 0, -1):
#                 pair = clean_no[i - 1:i + 1]
#                 if pair in main_dict:
#                     tag = list(main_dict[pair].keys())[0]
#                     message = main_dict[pair][tag]
#                 else:
#                     tag = "Good"
#                     message = "good"

#                 combinations_dict[percent] = {
#                     "pair": pair,
#                     "tag": tag,
#                     "message": message,
#                     "type": "percent"
#                 }
#                 percent -= 10

#             for i in range(len(clean_no) - 2):
#                 triplet = clean_no[i:i + 3]
#                 if triplet in main_dict:
#                     tag = list(main_dict[triplet].keys())[0]
#                     message = main_dict[triplet][tag]
#                     combinations_dict[f"special ({triplet})"] = {
#                         "pair": triplet,
#                         "tag": tag,
#                         "message": message,
#                         "type": "special"
#                     }


#             context["phone"] = phone_no
#             context["digit_sum"] = sum_of_digits
#             context["combinations"] = combinations_dict

#     return render(request, "index.html", context)


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     return redirect('login')

# @login_required
# def home_view(request):
#     if not request.user.has_access:
#         # return render(request, 'payment.html')
#         redirect('upload_payment')  # Redirect to payment view if no access
#     return redirect('index')  # Your main phone check logic

# # @login_required
# # def upload_payment_screenshot(request):
# #     if request.method == 'POST':
# #         form = PaymentForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             request.user.payment_screenshot = form.cleaned_data['screenshot']
# #             request.user.save()
# #             return render(request, 'thank_you.html')  # show "We'll verify soon" message
# #     else:
# #         form = PaymentForm()
# #     return render(request, 'upload_payment.html', {'form': form})

# @login_required
# def payment_view(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST, request.FILES)
#         if form.is_valid():
#             duration = int(form.cleaned_data['subscription_duration_days'])
#             screenshot = form.cleaned_data['screenshot']

#             user = request.user
#             user.subscription_start = date.today()
#             user.subscription_duration_days = duration
#             user.payment_screenshot = screenshot
#             user.save()

#             return render(request, 'thank_you.html')  # show "We'll verify soon" message
#     else:
#         form = PaymentForm()
#     return render(request, 'payment.html', {'form': form})




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .forms import SignUpForm, PaymentForm
from .models import CustomUser
# from .logic import main_dict  # if you're using your checker logic from here

@login_required
def index(request):
    if not request.user.has_access:
        return redirect('payment')

    context = {}
    if request.method == "POST":
        phone_no = request.POST.get("phone_number", "").strip()
        if len(phone_no) != 10 or not phone_no.isdigit():
            context["error"] = "Please enter a valid 10-digit phone number."
        else:
            sum_of_digits = sum(int(d) for d in phone_no)
            while sum_of_digits >= 10:
                sum_of_digits = sum(int(d) for d in str(sum_of_digits))

            clean_no = phone_no.replace("0", "")
            percent = 90
            combinations_dict = {}

            for i in range(len(clean_no) - 1, 0, -1):
                pair = clean_no[i - 1:i + 1]
                if pair in main_dict:
                    tag = list(main_dict[pair].keys())[0]
                    message = main_dict[pair][tag]
                else:
                    tag = "Good"
                    message = "good"

                combinations_dict[percent] = {
                    "pair": pair,
                    "tag": tag,
                    "message": message,
                    "type": "percent"
                }
                percent -= 10

            for i in range(len(clean_no) - 2):
                triplet = clean_no[i:i + 3]
                if triplet in main_dict:
                    tag = list(main_dict[triplet].keys())[0]
                    message = main_dict[triplet][tag]
                    combinations_dict[f"special ({triplet})"] = {
                        "pair": triplet,
                        "tag": tag,
                        "message": message,
                        "type": "special"
                    }

            context["phone"] = phone_no
            context["digit_sum"] = sum_of_digits
            context["combinations"] = combinations_dict

    return render(request, "index.html", context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    # if not request.user.has_access:
    #     return redirect('payment')
    # return redirect('index')
    return render(request, 'home.html')

@login_required
# def payment_view(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = request.user
#             user.subscription_start = date.today()
#             user.subscription_duration_days = form.cleaned_data['subscription_duration_days']
#             user.payment_screenshot = form.cleaned_data['payment_screenshot']
#             user.save()
#             return render(request, 'thank_you.html')
#     else:
#         form = PaymentForm()
#     return render(request, 'payment.html', {'form': form})

# def payment_view(request):
#     user = request.user

#     if user.has_access:
#         return render(request, 'payment.html', {'user': user, 'form': None})

#     if request.method == 'POST':
#         form = PaymentForm(request.POST, request.FILES)
#         if form.is_valid():
#             user.payment_screenshot = form.cleaned_data['payment_screenshot']
#             user.subscription_start = date.today()
#             user.subscription_duration_days = int(form.cleaned_data['duration'])
#             user.save()
#             return render(request, 'thank_you.html')
#     else:
#         form = PaymentForm()

#     return render(request, 'payment.html', {'user': user, 'form': form})

def payment_view(request):
    user = request.user

    # First handle the POST request
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            user.payment_screenshot = form.cleaned_data['payment_screenshot']
            user.subscription_start = date.today()
            user.subscription_duration_days = int(form.cleaned_data['duration'])
            user.save()
            return render(request, 'thank_you.html')  
    else:
        form = PaymentForm()

    # For both access/no access: show payment page (GET or failed POST)
    return render(request, 'payment.html', {'user': user, 'form': form if not user.has_access else None})
