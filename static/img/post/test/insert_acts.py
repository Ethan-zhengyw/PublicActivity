# coding=utf-8
from mongoengine import *
from activity import *
from user import *
import datetime
connect('activity')

tags = '爱心'
def example1():
	name = "衣旧暖心"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "有这样一群孩子，下值天真浪漫的年龄，本该享受生活的快乐，家庭的温馨，却因家庭贫困，过早的品偿着生少于的艰辛;\n他们买不起新的衣服，不敢奢望有游玩的假期，他们与出外打工的父母开离，他们甚至有病不敢就医.....他们偷偷羡慕和祈祷，羡慕同龄的人幸福和轻松，祈祷有一双手能给他们帮助和温暖。\n城市里的您，每年都在为怎么处理旧衣服而烦恼，留着占地方，扔了又可惜，送亲戚朋友又送不出手........\n山里的他们，每年都在为生计而烦恼，年收入不过千，孩子上不起学，老人看不起病，衣服残旧不堪......\n我们也许没有很高的收入，我们也许没有多余的存款，我们也许捐不起一所希望小学，但我们可以把我们不需要的旧物转给那些需要它们的人，这只需要我们的爱心。\n请需要处理旧衣服的人们但这里找寻旧衣服的去处，用我们的爱心给这些旧衣服增添新的光彩。希望大家行动起来，进我们的绵薄之力，帮到一些我们能帮到人的，这也是一种快乐。"
	host = "托爱公益事业发展中心"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/1.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example2():
	name = "为中国而教"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "我们以培养促进教育公平的领导者为使命，招募并输送优秀大学毕业生到农村学校或城市打工子弟学校任教两年，并为志愿者提供持续而系统的培训和支持，培养和集结关心教育的优秀人才，以此促进中国社会的进步！"
	host = "为中国而教项目"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/2.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example3():
	name = "特殊少儿家庭同乐日"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "厦门诺苗是一家由特殊少儿的家长发起的民间公益机构，从2009年开始，我们在厦门举办同乐日.\n时至今日，我们已将同乐日推广到厦门周边漳州，龙岩等地，并培训了国内各地20多个机构，并推动他们也举办同乐日。同乐日活动深深地得到特殊少儿、特殊少儿家长、社会公众、爱心企业、大学生志愿团体的认可和喜爱。"
	host = "厦门诺苗教育咨询有限公司"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/3.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example4():
	name = "情浓端午粽是有爱"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "发放端午节咸蛋、粽子爱心物资给粮道街、紫阳街、黄鹤楼街读书社区93户低保困难家庭。"
	host = "武汉爱心食物中心"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/4.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example5():
	name = "标致雪铁龙“绿色出行，低碳环保”儿童环境保护家庭教育项目"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "推广公众的道路交通安全和环境保护意识是标致雪铁龙集团在中国的一项重要工作。\n自2011年起，标致雪铁龙集团及标致雪铁龙基金会携手全国妇联心系系列活动组委会启动“绿色出行，低碳环保”儿童环境保护家庭教育活动，旨在为成长中的中国儿童树立绿色、环保的社会观和价值观，为中国社会实现节能环保和可持续发展做出贡献。\n2012年是标致雪铁龙集团携手全国妇联致力于儿童环保家庭教育项目的第二年，届时绿色安全脚步将陆续走进北京、上海、广州、武汉和深圳5座城市的700所幼儿园，共计超过50万名儿童及其家庭将从中受益。"
	host = "标致雪铁龙基金会"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/5.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example6():
	name = "博爱助学计划"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "为了弘扬“人道、博爱、奉献”的红十字精神，广泛动员社会资源资助贫困地区教育条件的改善，中国红十字基金会在教育领域倡导实施“博爱助学计划”公益项目。\n“博爱助学计划”的宗旨是：广泛动员社会力量，在贫困地区农村援建博爱小学，为贫困地区中小学捐赠博爱电脑教室和“红十字书库”，设立博爱助学金资助贫困大学生完成学业，协助政府改善贫困地区的办学条件。"
	host = "中国红十字基金会"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/6.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example7():
	name = "免费午餐计划"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "免费午餐计划是一项爱心公益活动，主要为贫困学生提供免费午餐，帮助每个家庭困难的孩子都能安心学习，快乐成长，享受社会的关爱。"
	host = "数十家媒体联合发起"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/7.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example8():
	name = "绿箱子环保计划——废弃手机及配件回收"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "中国移动携手摩托罗拉、诺基亚联合发起“绿箱子环保计划－－废弃手机及配件回收”公益行动。\n约 1000 家中国移动自办营业厅和摩托罗拉、诺基亚各约 150 家销售中心、维修服务中心将长期设立专门用于废弃手机及配件回收的“绿箱子”。\n手机用户可以选择就近地点将已经废弃的手机及各类配件投入其中。该行动所回收的废旧手机及配件将由中国移动、摩托罗拉、诺基亚三方共同委托专业的公司进行无害化处理，并对其中部分成分进行回收再利用。\n此次行动旨在探索建立废弃手机及配件回收体系倡导通信环保时尚生活，同时呼吁更多的通信企业和社会人士加入到该回收行动中来。 "
	host = "中国移动、摩托罗拉、诺基亚"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/8.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example9():
	name = "扬帆计划"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "扬帆计划是由民建中央委员汪延先生(新浪网创建人、董事长)发起和管理的公益助学项目，也是中华思源工程扶贫基金会的重要项目之一。\n它通过捐助课外图书、举行夏令营、开办扬帆班、援助优秀教师等活动，帮助偏远贫困地区的孩子增长见识、开拓视野，增强他们建设家乡的使命感，最终培养一批改变中国未来农村命运的关键人才。 "
	host = "中华思源工程扶贫基金会"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/9.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example10():
	name = "福特汽车环保奖"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "“福特汽车环保奖”是世界上规模最大的环保奖评比活动之一，授奖活动遍及50多个国家和地区，其前身是1983年在英国首次发起的“亨利·福特环保奖”，其宗旨是鼓励各阶层人士积极参与有助于保护本地环境和自然资源的活动。\n自2000年首次进入中国，十一年来，“福特汽车环保奖”已经成为中国目前由企业独立运作、卓有声誉的环保奖评选活动。\n迄今，“福特汽车环保奖”总计授予奖金1100万人民币，共有224个优秀环保团体和个人获得了奖金资助或提名鼓励，并为超过320家民间环保组织提供了能力建设培训。"
	host = "福特汽车环保奖组委会"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/10.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example11():
	name = "英德晨曦天使助学计划"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "天使助学计划英德市晨曦志愿者协会2014年推出的一项资助贫困学生生活费的计划。本计划在2014年7月12日正式推出。\n本计划的目标是保障贫困的乡镇困难户儿童完成最基本的九年义务教育。虽然现在九年义务教育已经普及，学校不再收取学费，但是在我们身边的乡镇，仍有许多适龄儿童因为家庭贫困，过着食不果腹衣不保暖的生活，导致适龄儿童无法完成九年义务教育学业。“天使助学计划”，目的在于保障这些儿童最基本的生活，让他们没有生活方面的后患可以专心学习。"
	host = "英德市晨曦志愿者协会"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/11.jpg"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def example12():
	name = "大地之爱-母亲水窖"
	create_time = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
	start_time = datetime.datetime.strptime('2015-03-21', '%Y-%m-%d')
	deadline = datetime.datetime.strptime('2015-03-31', '%Y-%m-%d')
	introduction = "干旱缺水是世界性的问题，中国西部是地球上主要干旱带之一，由于中国社会转型期的社会流动，妇女成为西部贫困干旱地区家庭的主要劳动力，她们不得不每日往返几里、几十里山路找回生命水。为了配合国家西部大开发战略以及全国妇联提出“举全国妇女之力，建西部美好家园”的号召，帮助西部妇女和群众解决饮用水困难.\n2000年由全国妇联、北京市政府、中央电视台主办，中国妇女发展基金会具体承办了“情系西部·共享母爱”世纪爱心行动，筹集善款1.16亿元，用于设立“大地之爱·母亲水窖”项目专项基金，并于2001年开始实施，深受社会各界的广泛赞誉。\n2001年10月“母亲水窖”项目被载入国务院《中国农村扶贫开发白皮书》，2001年底被评为中国女性十大新闻，2003年11月被评选为“中国十大公益品牌”之一，2005年11月被评为“中华慈善奖”。"
	host = "中国妇女发展基金会"
	creater_id = str(User.objects().first().id)
	location = "广州"
	isPass = 0
	post = "/img/post/test/12.png"
	activity = Activity(name=name,create_time=create_time,start_time=start_time,deadline=deadline,introduction=introduction,host=host,location=location,isPass=isPass,post=post, creater_id=creater_id, tags=tags)
	activity.save()

def insert_acts():
	example1()
	example2()
	example3()
	example4()
	example5()
	example6()
	example7()
	example8()
	example9()
	example10()
	example11()
	example12()
