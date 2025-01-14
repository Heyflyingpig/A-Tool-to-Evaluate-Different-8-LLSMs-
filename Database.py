import json
import numpy

data = {
    "math_question": [
        {
            "id": 1,  # 题目id
            "year": 2019,  # 题目所属年份
            "difficulty": "ez",  # 题目难度
            "type": "choice" ,  # 题型
            "number": "N1",  # 编号
            "Source": "新课标1", # 题目所属卷型
            "Description": [
                {
                    "Qu" : "已知集合M={x|-4<x<2}，N={x|x^2-x-6< 0}，则M∩N = () A．{x|-4<x<3}	B．{x|-4<x< 2}	C．{x|-2<x<2}	D．{x|2<x<3}  "
                }
            ],  # 题目描述
            "An": "C"  # 题目答案
        },  # 201901,1,ez
        {
            "id": 2,
            "year": 2019,
            "difficulty": "av",
            "type": "choice" ,
            "number": "N4",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu" : "古希腊时期，人们认为最美人体的头顶至肚脐的长度与肚脐至足底的长度之比是:$a = \\log_{2} 0.2$,b=2^0.2,c=0.2^0.3（a<b<c≈0.618，称为黄金分割比例)，著名的“断臂维纳斯”便是如此．此外，最美人体的头顶至咽喉的长度与咽喉至肚脐的长度之比也是a<c<b．若某人满足上述两个黄金分割比例，且腿长为105 cm，头顶至脖子下端的长度为26 cm，则其身高可能是A. 165 cm B. 175 cm C. 185 cm D. 190cm"

                }
            ],
            "An": "B"
        },  # 201901,4,av
        {
            "id": 3,
            "year": 2019,
            "difficulty": "me",
            "type": "choice" ,
            "number": "N10",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu" :r"""已知椭圆 \( C \) 的焦点为 \( F_1(-1,0)，F_2(1,0) $，过 \( F_2 $ 的直线与 \( C $ 交于 \( A $，$ B $ 两点．若 \( |AF_2| = 2|F_2B| $，\( |AB| = |BF_1| $，则 \( C $ 的方程为
\[ \begin{cases}
    \frac{x^2}{2} + y^2 = 1 \\
    \frac{x^2}{3} + \frac{y^2}{2} \\
    \frac{x^2}{4} + \frac{y^2}{3} \\
    \frac{x^2}{5} + \frac{y^2}{4}
\end{cases} \]
A．$\frac{x^2}{2} + y^2 = 1$ & B．$\frac{x^2}{3} + \frac{y^2}{2}$ & C．$\frac{x^2}{4} + \frac{y^2}{3}$ & D．$\frac{x^2}{5} + \frac{y^2}{4}$"
"""
                }
            ],
            "An": "B"
        },  # 201901,10,me
        {
            "id": 4,
            "year": 2019,
            "difficulty": "hard",
            "type": "choice" ,
            "number": "N12",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu" :r"""已知三棱锥 \( P -ABC $ 的四个顶点在球 \( O $ 的球面上，\( PA = PB = PC $，△\( ABC $ 是边长为 \( 2 $ 的正三角形，\( E $，\( F $ 分别是 \( PA $，\( PB $ 的中点，∠\( CEF $=90°，则球 \( O $ 的体积为
\[ \begin{cases}
    8\sqrt{6}\pi \\
    4\sqrt{6}\pi \\
    2\sqrt{6}\pi \\
    \sqrt{6}\pi
\end{cases} \]
A．$8\sqrt{6}\pi$ & B．$4\sqrt{6}\pi$ & C．$2\sqrt{6}\pi$ & D．$\sqrt{6}\pi$
"""
                }
            ],
            "An": "D"
        },  # 201901,12,ha

        {
            "id": 5,
            "year": 2019,
            "difficulty": "ez",
            "type": "gap" ,
            "number": "N13",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu" :r"""13．曲线 \( y = 3(x^2 + x)e^{-x} $ 在点 $(0,0)$ 处的切线方程为 ____________．"""
                }
            ],
            "An": "y=3x"
        },  # 201901,13,ez
        {
            "id": 6,
            "year": 2019,
            "difficulty": "av",
            "type": "gap" ,
            "number": "N14",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu" :r"""14．记 \( S_n $ 为等比数列 $\left\{a_n\right\}$ 的前 \( n $ 项和． 若 \( a_1=\frac{1}{3} $， \( a_4^2=a_6 $， 则 \( S_5=$______________．"""
                }
            ],
            "An": "121/3"
        },  # 201901,14,av
        {
                    "id": 7,
                    "year": 2019,
                    "difficulty": "me",
                    "type": "gap" ,
                    "number": "N15",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu" :r"""甲、乙两队进行篮球决赛，采取七场四胜制（当一队赢得四场胜利时，该队获胜，决赛  
结束）．根据前期比赛成绩，甲队的主客场安排依次为“主主客客主客主”．设甲队主场取
胜的概率为0.6，客场取胜的概率为0.5，且各场比赛结果相互独立，则甲队以4∶1获胜的概
率是____________
"""
                        }
                    ],
                    "An": "0.216"
                },  # 201901,15,me
        {
                    "id": 8,
                    "year": 2019,
                    "difficulty": "ha",
                    "type": "gap" ,
                    "number": "N16",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu" :r"""16．已知双曲线 \( C $：$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1(a>0,b>0)$ 的左、右焦点分别为 \( F_1 $，\( F_2 $，过 \( F_1 $ 的直线与 \( C $ 的两条渐近线分别交于 \( A $，\( B $ 两点．若 \( \overrightarrow{{F}_{1}A}=\overrightarrow{AB} $，\( \overrightarrow{{F}_{1}B}⋅\overrightarrow{{F}_{2}B}=0 $，则 \( C $ 的离心率为 ____________．
"""
                        }
                    ],
                    "An": "2"
                },  # 201901,16,ha

        {
                    "id": 9,
                    "year": 2019,
                    "difficulty": "ez",
                    "type": "comprehensive" ,
                    "number": "N17",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu" :r"""17．$\triangle ABC $ 的内角 \( A $，\( B $，\( C $ 的对边分别为 \( a $，\( b $，\( c $， 设
\[ (\sin B-\sin C)^2=sin^2 A-sin B sin C $．
\[ （1）求 \( A $；
\[ （2）若 $\sqrt{2a+b}=2c $， 求 \( sin C $.

"""
                        }
                    ],
                    "An": r"""\[ 【答案】 （1）$A=\frac{\pi}{3}$；（2）$sin C=\frac{\sqrt{6}+\sqrt{2}}{4}$．．
                    """
                },  # 201901,17,ez
        {
                    "id": 10,
                    "year": 2019,
                    "difficulty": "ez",
                    "type": "comprehensive" ,
                    "number": "N19  ",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu" :r"""19．已知抛物线 \( C $：$y^2=3x$ 的焦点为 \( F $， 斜率为$-\frac{3}{2}$ 的直线 \( l $ 与 \( C $ 的交点为 \( A $，\( B $， 与x轴的交点为 \( P $．
\[ （1）若 \( |AF|+|BF|=4 $，求 \( l $ 的方程；
\[ （2）若 $\overrightarrow{AP}=3\overrightarrow{PB}$， 求 \( |AB|$．
"""
                        }
                    ],
                    "An": r"""\[ 【答案】（1）$12x-8y-7=0$；（2）$\frac{4\sqrt{13}}{3}$．
                    """
                },  # 201901,19,av
        {
                    "id": 11,
                    "year": 2019,
                    "difficulty": "me",
                    "type": "comprehensive" ,
                    "number": "N20",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu" :r"""20．已知函数 \( f(x)=sin x-ln(1+x) $， \( f'(x) $ 为 \( f(x) $ 的导数．证明：
\[ （1）f'(x) $ 在区间$ (-1,\frac{\pi}{2}) $存在唯一极大值点；
\[ （2）\( f(x) $有且仅有2个零点．
"""
                        }
                    ],
                    "An": r"""20．[详解]（1）由意得：\( f(x)=cos x+\frac{1}{x+1} $， \( x∈(-1,\frac{\pi}{2}) $
\[ ∴g'(x)=-sin x+\frac{1}{(x+1)^2} $， \( x∈(-1,\frac{\pi}{2}) $，
\[ ∴\frac{1}{(x+1)^2} $在$ (-1,\frac{\pi}{2}) $上单调递减， \( a_{n+1}-a_n=\frac{1}{n(n+1)} $， \( a_n $在$ (-1,\frac{\pi}{2}) $上单调递增， \( a_n $在$ (-1,\frac{\pi}{2}) $上单调递减
\[ 又∵g'(\frac{\pi}{2})=-sin \frac{\pi}{2}+\frac{1}{(\frac{\pi}{2}+1)^2}=-1+\frac{1}{(\frac{\pi}{2}+1)^2} < 0 $， \( g'(0)=-sin 0+1=1 > 0 $， \( g'(\frac{\pi}{2})=-\sin \frac{\pi}{2}+\frac{4}{\pi+2}=\frac{4}{\pi+2}-1 < 0 $，
\[ ∴∃x_0∈(0,\frac{\pi}{2}) $，使得\( g'(x_0)=0 $，
\[ 即\( g(x) $在$ (-1,x_0) $上单调递增，在$ (x_0,\frac{\pi}{2}) $上单调递减
\[ 则\( x=x_0 $为\( g(x) $唯一的极大值点
\[ 即\( f'(x) $在区间$ (-1,\frac{\pi}{2}) $存在唯一的极大值点\( x_0 $．
\[ （2）由（1）知：\( f'(x)=cos x+\frac{1}{x+1} $， \( x∈(-1,∞)
\[ ①当\( x∈(-1,0] $时，由（1）可知\( f'(x) $在$ (-1,0] $上单调递增
\[ ∴\( f'(x)\leqslant f'(0)=0 $∴\( f'(x) $在$ (-1,0] $上单调递减
\[ 又\( f'(0)=0 $∴\( f(x) $在$ (-1,0] $上的唯一零点
\[ ②当\( x∈(0,\frac{\pi}{2}] $时，\( f'(x) $在$ (0,x_0) $上单调递增，在$ (x_0,\frac{\pi}{2}) $上单调递减
\[ 又\( f'(x_0)=0 $∴\( f'(x) $在$ (0,x_0) $上单调递增，此时\( f(x)>f(0)=0 $，不存在零点
\[ 又\( f'(\frac{\pi}{2})=\cos \frac{\pi}{2}-\frac{2}{\pi+2}=-\frac{2}{\pi+2} < 0 $，
\[ ∴∃x_0∈(0,\frac{\pi}{2}) $，使得\( f'(x_0)=0 $，
\[ 即\( f(x) $在$ (x_0,\frac{\pi}{2}) $上单调递减，在$ (\frac{\pi}{2},π) $上单调递增
\[ 又\( f(x_0)>f(0)=0 $， \( f(\frac{\pi}{2})=sin \frac{\pi}{2}-ln(\pi+1)=-ln(\pi+1) < 0 $，
\[ ∴\( f(x) $在$ (\frac{\pi}{2},π) $上存在唯一零点
\[ ③当\( x∈[\frac{\pi}{2},π] $时，\( sin x $单调递减， \( -ln(x+1) $单调递减
\[ ∴\( f(x) $在$ [\frac{\pi}{2},π] $上单调递减
\[ 又\( f(\frac{\pi}{2}) > 0 $， \( f(π)=sin π-ln(\pi+1)=-ln(\pi+1) < 0 $，
\[ 即\( f(x) $在$ (\frac{\pi}{2},π) $上存在唯一零点
\[ ④当\( x∈(π,∞) $时，\( sin x∈[-1,1] $， \( ln(x+1)>ln(\pi+1)>ln e=1 $，
\[ ∴sin x-ln(x+1) < 0 $即\( f'(x) $在$ (π,∞) $上不存在零点
\[ 综上所述：\( f(x) $有且仅有两个零点
                    """
                },  # 201901,20,me
        {
                    "id": 12,
                    "year": 2019,
                    "difficulty": "ha",
                    "type": "comprehensive" ,
                    "number": "N21",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu": r"""21．为了治疗某种疾病，研制了甲、乙两种新药，希望知道哪种新药更有效，为此进行动物试验．试验方案如下：每一轮选取两只白鼠对药效进行对比试验．对于两只白鼠，随机选一只施以甲药，另一只施以乙药．一轮的治疗结果得出后，再安排下一轮试验．当其中一种药治愈的白鼠比另一种药治愈的白鼠多4只时，就停止试验，并认为治愈只数多的药更有效．为了方便描述问题，约定：对于每轮试验，若施以甲药的白鼠治愈且施以乙药的白鼠未治愈则甲药得1分，乙药得−1分；若施以乙药的白鼠治愈且施以甲药的白鼠未治愈则乙药得1分，甲药得−1分；若都治愈或都未治愈则两种药均得0分．甲、乙两种药的治愈率分别记为 \( α $和 \( β $，一轮试验中甲药的得分记为 \( X $．
\[ （1）求 \( X $的分布列；
\[ （2）若甲药、乙药在试验开始时都赋予4分， \( p_i(i=0,1,…,8) $表示“甲药的累计得分为 \( i $时最终认为甲药比乙药更有效”的概率，则 \( p_0=0 $， \( p_8=1 $， \( p_i=aP(X=-1)+bP(X=0)+cP(X=1) $（\( i=1,2,…,7），其中 \( a=P(X=-1)， \( b=P(X=0)， \( c=P(X=1) $．假设 \( α=0.5 $， \( β=0.8 $．
\[ （i）证明： \( {p}_{i+1}-{p}_{i}(i=0,1,2,…,7) $为等比数列；
\[ （ii）求 \( p_4 $，并根据 \( p_4 $的值解释这种试验方案的合理性．
"""
                        }
                    ],
                    "An": r"""首先确定X所有可能的取值，再来计算出每个取值对应的概率，从而可得分布列；
（2）（i）求解出, , abc的取值，可得p_i = 0.4 * p_{i-1} + 0.5 * p_i + 0.1 * p_{i+1}  # (i = 1, 2, ..., 7)从而
整理出符合等比数列定义的形式，问题得证；（ii）列出证得的等比数列的通项公式，采
用累加的方式，结合p_8和P_0
 p的值可求得p_1,再次利用累加法可求出p_4
\begin{table}[h]
    \centering
    \begin{tabular}{|c|c|}
        \hline
        $X$ & $-1$ & $0$ & $1$ \\
        \hline
        $P(X)$ & $\left(1-\alpha\right)\beta$ & $\alpha\beta+\left(1-\alpha\right)\left(1-\beta\right)$ & $\alpha\left(1-\beta\right)$ \\
        \hline
    \end{tabular}
    \caption{分布列}
\end{table}

\begin{equation*}
    (2) \quad \because \alpha=0.5, \quad \beta=0.8
\end{equation*}

\begin{equation*}
    \therefore a=0.5\times0.8=0.4, \quad b=0.5\times0.8+0.5\times0.2=0.5, \quad c=0.5\times0.2=0.1
\end{equation*}

\begin{equation*}
    (\text{i}) \quad \because p_i=aq_{i-1}+bp_i+cq_{i+1}(i=1,2,\cdots,7)
\end{equation*}

\begin{equation*}
    \text{即 }p_i=0.4q_{i-1}+0.5p_i+0.1q_{i+1}(i=1,2,\cdots,7)
\end{equation*}

\begin{equation*}
    \text{整理可得: }5p_i=4q_{i-1}+q_{i+1}(i=1,2,\cdots,7) \quad \therefore p_{i+1}-p_i=4(p_i-p_{i-1})(i=1,2,\cdots,7)
\end{equation*}
                    """
                },  # 201901,21,ha

        {
            "id": 13,
            "year": 2019,
            "difficulty": "ez",
            "type": "choice" ,
            "number": "N1",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""math_expression = r"A=\{ x | x^2-5x+6>0 \}, \quad B=\{ x | x-1<0 \}"
intersection = r"A \cap B \Leftrightarrow"
option_A = r"(-\infty, 1)"
option_B = r"(-2, 1)^{\Leftrightarrow}"
option_C = r"(-3, -1)"
option_D = r"(3, +\infty)^{\Leftrightarrow}"
                    """
                }
            ],
            "An": "A"
        },  # 201902,1,ez
        {
            "id": 14,
            "year": 2019,
            "difficulty": "av",
            "type": "choice" ,
            "number": "N4",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
4. 2019年 1月 3日嫦娥四号探测器成功实现人类历史上首次月球背面软着陆,我国航天事业取得又一重大成就,实现月球背面软着陆需要解决的一个关键技术问题是地面与探测器的通讯联系.为解决这个问题,发射了嫦娥四号中继星“鹊桥”,鹊桥沿着围绕地月拉格朗日  L2  点的轨道运行.  L2  点是平衡点,位于地月连线的延长线上.设地球质量为 M1  ,月球质量为  M2  ,地月距离为 R,  L2  点到月球的距离为 r,根据牛顿运动定律和万有引力定律, r满足方程:

\[
\frac{M_1}{(R+r)^2}+\frac{M_2}{r^2}=(R+r)\frac{M_1}{R^3}.
\]

设  α=\frac{r}{R}  ,由于  α  的值很小,因此在近似计算中  \frac{3\alpha^3+3\alpha^4+\alpha^5}{(1+\alpha)^2}\approx 3\alpha^3  ,则 r的近似值

为

A. \sqrt{\frac{M_2}{M_1}} R

B. \sqrt{\frac{M_2}{2 M_1}} R

C. \sqrt[3]{\frac{3 M_2}{M_1}} R

D. \sqrt[3]{\frac{M_2}{3 M_1}} R                   
                    """
                }
            ],
            "An": "D"
        },  # 201902,4,av
        {
            "id": 15,
            "year": 2019,
            "difficulty": "me",
            "type": "choice",
            "number": "N10",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
10. 已知  $a\\in\\left(0,\\frac{\\pi}{2}\\right), 2\\sin 2\\alpha=\\cos 2\\alpha+1$  ,则 sin  $\\alpha=$ 

第6页|共22页

A.  $\\frac{1}{5}$ 

B.\\sqrt{\\frac{5}{5}} 

C.\\sqrt{\\frac{5}{2}} 

D.\\frac{5}{5}
        """
                }
            ],
            "An": "B"
        },  # 201902,10,me
        {
            "id": 16,
            "year": 2019,
            "difficulty": "hard",
            "type": "choice",
            "number": "N12",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
设函数 f(x)的定义域为 R,满足  $f(x+1)=2 f(x)$  ,且当  $x\\in(0,1]$  时,

 $f(x)=x(x-1)$  .若对任意  $x\\in(-\\infty, m]$  ,都有  $f(x)\\geq-\\frac{8}{9}$  ,则 m的取值范围是

A.  $\\left(-\\infty,\\frac{9}{4}\\right]$ 

B. $$\\left(-\\infty,\\frac{7}{3}\\right]$$

C. $$\\left(-\\infty,\\frac{5}{2}\\right]$$

D. $$\\left(-\\infty,\\frac{8}{3}\\right]$$
        """
                }
            ],
            "An": "B"
        },  # 201902,12,ha

        {
            "id": 17,
            "year": 2019,
            "difficulty": "ez",
            "type": "gap",
            "number": "N13",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""我国高铁发展迅速，技术先进．经统计，在经停某站的高铁列车中，有10个车次的正点率为0.97，有20个车次的正点率为0.98，有10个车次的正点率为0.99，则经停该站高铁列车所有车次的平均正点率的估计值为___________."""
                }
            ],
            "An": "0.98"
        },  # 201902,13,ez
        {
            "id": 18,
            "year": 2019,
            "difficulty": "av",
            "type": "gap",
            "number": "N14",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu" :r"""
已知f(x)是奇函数，且当x<0 时，f(x)=-ea.若f(ln2)=8，则α=
"""
                }
            ],
            "An": "-3"
        },  # 201902,14,av
        {
                    "id": 19,
                    "year": 2019,
                    "difficulty": "me",
                    "type": "gap" ,
                    "number": "N15",
                    "Source": "新课标2",
                    "Description": [
                        {
                            "Qu" :r"""15. VABC的内角 A,B,C的对边分别为 a,b,c.若  $b=6, a=2c, B=\\frac{\\pi}{3}$  ,则VABC的面积为$$.
"""
                        }
                    ],
                    "An": "6\\sqrt{2}"
                },  # 201902,15,me
        {
                    "id": 20,
                    "year": 2019,
                    "difficulty": "ha",
                    "type": "gap" ,
                    "number": "N16",
                    "Source": "新课标2",
                    "Description": [
                        {
                            "Qu" :r"""中国有悠久的金石文化，印信是金石文化的代表之一．印信的形状多为长方体、正方体或圆柱体，但南北朝时期的官员独孤信的印信形状是“半正多面体”（图1）.半正多面体是由两种或两种以上的正多边形围成的多面体.半正多面体体现了数学的对称美．图2是一个棱数为48的半正多面体，它的所有顶点都在同一个正方体的表面上，且此正方体的棱长为1．则该半正多面体共有________个面，其棱长为_________．
                        """,
                            "picture": "Images\2019\20190216.png"
                        }
                    ],
                    "An": " (1). 共26个面.    (2) 棱长为//sqrt{2}-1"
                },  # 201902,16,ha

        {
                    "id": 21,
                    "year": 2019,
                    "difficulty": "ez",
                    "type": "comprehensive" ,
                    "number": "N18 ",
                    "Source": "新课标2",
                    "Description": [
                        {
                            "Qu": r"""11分制乒乓球比赛，每赢一球得1分，当某局打成10:10平后，每球交换发球权，先多得2分的一方获胜，该局比赛结束.甲、乙两位同学进行单打比赛，假设甲发球时甲得分的概率为0.5，乙发球时甲得分的概率为0.4，各球的结果相互独立.在某局双方10:10平后，甲先发球，两人又打了X个球该局比赛结束.
（1）求P（X=2）；
（2）求事件“X=4且甲获胜”的概率. 
"""
                        }
                    ],
                    "An": r"""\[ 【答案】 （1）0.5（2）0.1
                    """
                },  # 201902,18,ez
        {
                    "id": 22,
                    "year": 2019,
                    "difficulty": "av",
                    "type": "comprehensive" ,
                    "number": "N19",
                    "Source": "新课标2",
                    "Description": [
                        {
                            "Qu" :r"""已知数列  $\\left\\{a_n\\right\\}$  和  $\\left\\{b_n\\right\\}$  满足  $a_1=1, b_1=0, 4 a_{n+1}=3 a_n-b_n+4, 4 b_{n+1}=3 b_n-a_n-4$  .

(1)证明:  $\\left\\{a_n+b_n\\right\\}$  是等比数列,  $\\left\\{a_n-b_n\\right\\}$  是等差数列;

(2)求  $\\left\\{a_n\\right\\}$  和  $\\left\\{b_n\\right\\}$  的通项公式.
"""
                        }
                    ],
                    "An": r"""\[ 【答案】（1）$12x-8y-7=0$；（2）$\frac{4\sqrt{13}}{3}$．
                    """
                },  # 201902,19,av
        {
                    "id": 23,
                    "year": 2019,
                    "difficulty": "me",
                    "type": "comprehensive",
                    "number": "N20",
                    "Source": "新课标2",
                    "Description": [
                        {
                            "Qu": r"""### 已知函数  $f(x)=\\ln x-\\frac{x+1}{x-1}$  .

(1)讨论  $f(x)$  的单调性,并证明  $f(x)$

(2)设  $x_0$  是  $f(x)$  的一个零点,证明曲线  $y=\\ln x$  在点  $A\\left(x_0,\\ln x_0\\right)$  处的切线也是曲线  $y=e^x$ 的切线.
"""
                        }
                    ],
                    "An": r"""(1)对函数  $f(x)$  求导,结合定义域,判断函数的单调性;

(2)先求出曲线  $y=\\ln x$  在  $A\\left(x_0,\\ln x_0\\right)$  处的切线 l,然后求出当曲线  $y=e^x$  切线的斜率与 l斜率相等时.证明曲线  $y=e^x$  切线  $l^{\prime}$  在纵轴上的截距与  $l^{\prime}$  在纵轴的截距相等即可.

[详解(1)函数 f(x)的定义域为  $(0,1)\\cup(1,+\\infty)$  .

 $f(x)=\\ln x-\\frac{x+1}{x-1}\\Rightarrow f^{\prime}(x)=\\frac{x^2+1}{x(x-1)^2}$  .因为函数  $f(x)$  的定义域为  $(0,1)\\cup(1,+\\infty)$  .所以 $f^{\prime}(x)>0$  .因此函数  $f(x)$  在  $(0,1)$  和  $(1,+\\infty)$  上是单调增函数;

$$\\frac{1}{e}+1$$当  $x\\in(0,1)$  .时,  $x\\rightarrow 0, y\\rightarrow-\\infty$  ,而  $f\\left(\\frac{1}{e}\\right)=\\ln\\frac{1}{e}$  $=\\frac{2}{e-1}>0$  .显然当  $x\\in(0,1)$  .$$\\frac{1}{e}-\\frac{1}{e}-1$$e-1

函数  $f(x)$  有零点,而函数  $f(x)$  在  $x\\in(0,1)$  上单调速增,故当  $x\\in(0,1)$  时,函数  $f(x)$  有唯一的零点:

当  $x\\in(1,+\\infty)$  时.  $f(e)=\\ln e-\\frac{e+1}{e-1}=\\frac{-2}{e-1}<0, f\\left(e^2\\right)=\\ln e^2-\\frac{e^2+1}{e^2-1}=\\frac{e^2-3}{e^2-1}>0.$ 

因为  $f(e)\\cdot f\\left(e^2\\right)<0$  ,所以函数  $f(x)$  在  $\\left(e, e^2\\right)$  必有一零点.而函数  $f(x)$  在  $(1,+\\infty)$  上是单调递增,故当  $x\\in(1,+\\infty)$  时,函数  $f(x)$  有唯一的零点

综上所述,函数  $f(x)$  的定义域  $(0,1)\\cup(1,+\\infty)$  内有 2个零点;

(2)因为  $x_0$  是  $f(x)$  的一个零点,所以  $f\\left(x_0\\right)=\\ln x_0-\\frac{x_0+1}{x_0-1}=0\\Rightarrow\\ln x_0=\\frac{x_0+1}{x_0-1}$  $y=\\ln x\\Rightarrow y^{\prime}=\\frac{1}{x}$  .所以曲线  $y=\\ln x$  在  $A\\left(x_0,\\ln x_0\\right)$  处的切线 l的斜率  $k=\\frac{1}{x_0}$  .故曲线 $y=\\ln x$  在  $A\\left(x_0,\\ln x_0\\right)$  处的切线 l的方程为:  $y-\\ln x_0=\\frac{1}{x_0}\\left(x-x_0\\right)$  而  $\\ln x_0=\\frac{x_0+1}{x_0-1}$  ,所以 l的方程为  $y=\\frac{x}{x_0}+\\frac{2}{x_0-1}$  .它在纵轴的截距为  $\\frac{2}{x_0-1}$  .

设曲线  $y=e^y$  的切点为  $B\\left(x_1, e^{x_0}\\right)$  .过切点为  $B\\left(x_1, e^{x_1}\\right)$  切线  $l^{\prime}, y=e^x\\Rightarrow y^{\prime}=e^x$  .所以在 $y=\\ln x$  在  $A\\left(x_0,\\ln x_0\\right)$  处的切线 l的方程为:  $y-\\ln x_0=\\frac{1}{x_0}\\left(x-x_0\\right)$  而  $\\ln x_0=\\frac{x_0+1}{x_0-1}$  ,所以 l

的方程为  $y=\\frac{x}{x_0}+\\frac{2}{x_0-1}$  ,它在纵轴的截距为  $\\frac{2}{x_0-1}$  .切线  $l^{\prime}$  在纵轴的截距为  $b_1=e^{x_1}\\left(1-x_1\\right)=e^{-\\ln x_0}\\left(1+\\ln x_0\\right)=\\frac{1}{x_0}\\left(1+\\ln x_0\\right)$  .而  $\\ln x_0=\\frac{x_0+1}{x_0-1}$  .所以  $b_1=\\frac{1}{x_0}\\left(1+\\frac{x_0+1}{x_0-1}\\right)=\\frac{2}{x_0-1}$  .直线  $l, l^{\prime}$  的斜率相等,在纵轴上的截距也相等,因此直线l,l重合,故曲线  $y=\\ln x$  在  $A\\left(x_0,\\ln x_0\\right)$  处的切线也是曲线  $y=e^x$  的切线.


                    """
                },  # 201902,20,me
        {
                    "id": 24,
                    "year": 2019,
                    "difficulty": "ha",
                    "type": "comprehensive",
                    "number": "N21",
                    "Source": "新课标2",
                    "Description": [
                        {
                            "Qu": r"""已知点 A(-2,0), B(2,0),动点 M(x, y)满足直线 A M与 B M的斜率之积为  $-\\frac{1}{2}$  .记 M的轨迹为曲线C.

(1)求 C的方程,并说明 C是什么曲线;

(2)过坐标原点的直线交 C于 P, Q两点,点 P在第一象限,  $P E\\perp x$  轴,垂足为 E,连结 Q E并延长交 C于点 G.

(i)证明:  $\\Delta P Q G$  是直角三角形;

(ii)求  $\\Delta P Q G$  面积的最大值.
"""
                        }
                    ],
                    "An": r"""(1)分别求出直线  $AM$  与 $BM$  的斜率,由已知直线  $AM$  与 $BM$  的斜率之积为  $-\\frac{1}{2}$  ,可以得到等式，化简可以求出曲线C的方程，注意直线AM与BM有斜率的条件;

(2)(1)设出直线 $PQ$ 的方程，与椭圆方程联立，求出 $P$, $Q$ 间点的坐标，进而求出点 $E$ 的坐标，求出直线 $QE$ 的方程，与椭圆方程联立，利用相与系数关系来求出 $G$ 的坐标，再求出直线 $PQ$ 的斜率，计算  $k_{PQ} \\cdot k_{QG}$  的值，就可以证明出 $\Delta PQG$ 是直角三角形

(2)由(1)可知 $P$, $Q$, $G$ 三点坐标。 $\Delta PQG$ 是直角三角形。求出 $PQ$, $QG$ 的长，利用面积公式求出 $\Delta PQG$ 的面积，利用导数求出面积的最大值。

[详解](1)直线 $AM$ 的斜率为  $\\frac{y}{x+2}(x\\neq -2)$  ,直线 $BM$ 的斜率为  $\\frac{y}{x-2}(x\\neq 2)$  ,由题意可知:  $\\frac{y}{x+2} \\cdot \\frac{y}{x-2} = -\\frac{1}{2}$  ,化简得 $x^2 + 2y^2 = 4$  $(x\\neq \\pm2)$  ,所以曲线 $C$ 是以坐标原点为中心，焦点在x轴上，不包括左右顶点的椭圆，其方程为 $\\frac{x^2}{4} + \\frac{y^2}{2} = 1$  $(x\\neq \\pm2)$。

(2)(1)直线 $PQ$ 的方程为 $y=kx$  ,由题意可知 $k>0$  ,直线 $PQ$ 的方程与椭圆方程联立，即 $\\left\\{\\begin{array}{l} y=kx \\\\ x^2+2y^2=4 \\end{array}\\right.$  ,解得 $P\\left(\\frac{2}{\\sqrt{2k^2+1}}, \\frac{2k}{\\sqrt{2k^2+1}}\\right)$  , $Q\\left(\\frac{-2}{\\sqrt{2k^2+1}}, \\frac{-2k}{\\sqrt{2k^2+1}}\\right)$  ,因此点 $E$ 的坐标为 $(\\frac{2}{\\sqrt{2k^2+1}}, 0)$。

直线 $QE$ 的斜率为 $k_{QE}=\\frac{k}{2}$  ,可得直线 $QE$ 方程为 $y=\\frac{k}{2}x-\\frac{k}{\\sqrt{2k^2+1}}$  ,与椭圆方程联立。

解得 $G\\left(\\frac{6k^2+4}{(k^2+2)\\sqrt{2k^2+1}}, \\frac{2k^2}{(k^2+2)\\sqrt{2k^2+1}}\\right)$。

直线 $PG$ 的斜率为 $k_{PG}=\\frac{2k^2}{(k^2+2)\\sqrt{2k^2+1}}\\cdot \\frac{2}{\\sqrt{2k^2+1}} = -\\frac{1}{k}$  ,因为 $k_{PQ} \\cdot k_{PG} = k \\cdot (-\\frac{1}{k}) = -1$  ,所以 $PQ \\perp PG$，因此 $\Delta PQG$ 是直角三角形;

(2)由(1)可知：$P\\left(\\frac{2}{\\sqrt{2k^2+1}}, \\frac{2k}{\\sqrt{2k^2+1}}\\right)$  , $Q\\left(\\frac{-2}{\\sqrt{2k^2+1}}, \\frac{-2k}{\\sqrt{2k^2+1}}\\right)$  , $G\\left(\\frac{6k^2+4}{(k^2+2)\\sqrt{2k^2+1}}, \\frac{2k^2}{(k^2+2)\\sqrt{2k^2+1}}\\right)$  .

$PQ=\\sqrt{\\left(\\frac{2}{\\sqrt{2k^2+1}}-\\frac{-2}{\\sqrt{2k^2+1}}\\right)^2+\\left(\\frac{2k}{\\sqrt{2k^2+1}}-\\frac{-2k}{\\sqrt{2k^2+1}}\\right)^2}=\\frac{4\\sqrt{1+k^2}}{\\sqrt{2k^2+1}}$.

$PG=\\sqrt{\\left(\\frac{6k^2+4}{(k^2+2)\\sqrt{2k^2+1}}-\\frac{2}{\\sqrt{2k^2+1}}\\right)^2+\\left(\\frac{2k^2}{(k^2+2)\\sqrt{2k^2+1}}-\\frac{2k}{\\sqrt{2k^2+1}}\\right)^2}=\\frac{4k\\sqrt{k^2+1}}{(k^2+2)\\sqrt{2k^2+1}}$.

$S_{\\Delta PQG}=\\frac{1}{2}\\times PQ\\times PG=\\frac{1}{2}\\times \\frac{4\\sqrt{1+k^2}}{\\sqrt{2k^2+1}}\\times \\frac{4k\\sqrt{k^2+1}}{(k^2+2)\\sqrt{2k^2+1}}=\\frac{8(k^3+k)}{2k^4+5k^2+2}$.

$S=\\frac{-8(k+1)(k-1)(2k^4+3k^2+2)}{(2k^4+5k^2+2)}$, 因为 $k>0$, 所以当 $0<k<1$ 时, $S>0$, 函数 $S(k)$ 在 $(0,1)$ 上单调递增，在 $(1,+\\infty)$ 上单调递减，所以当 $k=1$ 时，$S$ 取得最大值。
                    """
                },  # 201902,21,ha

        {
            "id": 25,
            "year": 2020,
            "difficulty": "ez",
            "type": "choice" ,
            "number": "N1",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu": r"""### 1. 若z=1+i，则|z^2-2z|=()

A. 0
B. 1
C. √2
D. 2
                    """
                }
            ],
            "An": "D"
        },  # 202001,1,ez
        {
            "id": 26,
            "year": 2020,
            "difficulty": "av",
            "type": "choice" ,
            "number": "N4",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu": r"""
已知A为抛物线C: y²=2px(p>0)上一点,点A到C的焦点的距离为12,到y轴的距离为9,则p=(\quad)
A. 2
B. 3
C. 6
D. 9              
                    """
                }
            ],
            "An": "C"
        },  # 202001,4,av
        {
            "id": 27,
            "year": 2020,
            "difficulty": "me",
            "type": "choice",
            "number": "N10",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu": r"""
已知A,B,C为球O的球面上的三个点,  $\\odot O_1$  为  $\\triangle ABC$  的外接圆,若  $\\odot O_1$  的面积为  $4\\pi$ 

，  $AB=BC=AC=OO_1$  ，则球O的表面积为()

A.  $64\\pi$ 

B. 48π

C. 36π

D. $32\\pi$
        """
                }
            ],
            "An": "A"
        },  # 202001,10,me
        {
            "id": 28,
            "year": 2019,
            "difficulty": "hard",
            "type": "choice",
            "number": "N12",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu": r"""
12. 若  $2^{a}+\\log_{2} a=4^{b}+2\\log_{4} b$  ,则()

A. a > 2b

B. a < 2b

C. a > b^2

D. a < b^2
        """
                }
            ],
            "An": "B"
        },  # 202001,12,ha

        {
            "id": 29,
            "year": 2020,
            "difficulty": "ez",
            "type": "gap",
            "number": "N13",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu" :r"""
                    $$2x + y - 2 \leq 0$$

若x, y满足约束条件
$$\left\{\begin{array}{l}
x - y - 1 \geq 0, \\y + 1 \geq 0, \\2x + y - 2 \leq \end{array}\right.$$
则 z = x + 7y 的最大值为
$$y + 1 \geq 0,$$
"""
                }
            ],
            "An": "1"
        },  # 202001,13,ez
        {
            "id": 30,
            "year": 2020,
            "difficulty": "av",
            "type": "gap" ,
            "number": "N14",
            "Source": "新课标1",
            "Description": [
                {
                    "Qu" :r"""
                   设 a, b为单位向量,且 $|a+b|=1$,则 $|a-b|=$
                   """
                }
            ],
            "An": r"$\sqrt{3}$"
        },  # 202001,14,av
        {
                    "id": 31,
                    "year": 2020,
                    "difficulty": "me",
                    "type": "gap" ,
                    "number": "N15",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu" : r"""15. 已知 F为双曲线 $C: \\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1(a > 0, b > 0)$ 的右焦点, A为 C的右顶点, B为 C上的点,且 BF垂直于x轴.若AB的斜率为3,则C的离心率为
"""
                        }
                    ],
                    "An": "2"
                },  # 202001,15,me
        {
                    "id": 32,
                    "year": 2019,
                    "difficulty": "ha",
                    "type": "gap",
                    "number": "N16",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu" :r"""### 16. 如图,在三棱锥 P-ABC的平面展开图中, $AC=1,\quad AB=AD=\sqrt{3}, AB\\perp AC, AB\\perp AD,\\angle CAE=30^{\circ}$  ,则 $\cos\\angle FCB=$
                            """,
                            "picture": "Images\2020\20200116.png"
                        }
                    ],
                    "An": "-(1/4)"
                },  # 202001,16,ha

        {
                    "id": 33,
                    "year": 2020,
                    "difficulty": "ez",
                    "type": "comprehensive",
                    "number": "N17",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu": r"""
                            17. 设 $\left\{a_n\right\}$ 是公比不为 1的等比数列, $a_1$ 为 $a_2$, $a_3$ 的等差中项.

(1) 求 $\left\{a_n\right\}$ 的公比;

(2) 若 $a_1=1$, 求数列 $\left\{n a_n\right\}$ 的和.
"""
                        }
                    ],
                    "An": r"""$$(1)-2;\quad(2) S_{n}=\frac{1-(1+3n)(-2)^{n}}{9}.$$
                    """
                },  # 202001,17,ez
        {
                    "id": 34,
                    "year": 2020,
                    "difficulty": "av",
                    "type": "comprehensive",
                    "number": "N19",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu" :r"""
                            甲、乙、丙三位同学进行羽毛球比赛,约定赛制如下:累计负两场者被淘汰;比赛前抽签决定首先比赛的两人，另一人轮空;每场比赛的胜者与轮空者进行下一场比赛，负者下一场轮空,直至有一人被淘汰;当一人被淘汰后,剩余的两人继续比赛,直至其中一人被淘汰,另一人最终获胜，比赛结束.经抽签，甲、乙首先比赛，丙轮空.设每场比赛双方获胜的概率都为 $\frac{1}{2}$ ,

(1) 求甲连胜四场的概率;

(2) 求需要进行第五场比赛的概率;

(3) 求丙最终获胜的概率.
"""
                        }
                    ],
                    "An": r"""1）$1/16$；（2）$3/4$．(3)$7/16$
                    """
                },  # 202001,19,av
        {
                    "id": 35,
                    "year": 2020,
                    "difficulty": "me",
                    "type": "comprehensive",
                    "number": "N20",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu": r"""### $$x^2$$20. 已知 A、 B分别为椭圆 E: $$\frac{x^2}{a^2} + y^2 = 1(a > 1)$$ 的左、右顶点, G为E的上顶点, $$\overrightarrow{AG} \cdot \overrightarrow{GB} = 8$$, P为直线 $x = 6$ 上的动点, PA与E的另一交点为C, PB与E的另一交点为D. (1)求E的方程;

(2) 证明: 直线CD过定点.
"""
                        }
                    ],
                    "An": r"""[答案](1) $$\frac{x^2}{9} + y^2 = 1$$; (2) 证明详见解析.
(1) 由已知可得: $A(-a, 0)$, B(a, 0), G(0,1), 即可求得 $$\overrightarrow{AG} \cdot \overrightarrow{GB} = a^2 - 1$$, 结合已知即可求得: $a^2 = 9$, 问题得解.
(2) 设 $P(6, y_0)$, 可得直线 AP的方程为: $y = \frac{y_0}{9}(x + 3)$, 联立直线 AP的方程与椭圆方程即可求得点 C的坐标为 $\left(\frac{-3y_0^2 + 27}{y_0^2 + 9}, \frac{6y_0}{y_0^2 + 9}\right)$, 同理可得点 D的坐标为 $\left(\frac{3y_0^2 - 3}{y_0^2 + 1}, \frac{-2y_0}{y_0^2 + 1}\right)$, 即可表示出直线 CD的方程, 整理直线 CD的方程可得:
4$$y = \frac{4y_0}{3(3 - y_0^2)}(x - \frac{3}{2})$$, $$y = \frac{4y_0}{3(3 - y_0^2)}(x - \frac{3}{2})$$, 命题得证.
                    """
                },  # 202001,20,me
        {
                    "id": 36,
                    "year": 2020,
                    "difficulty": "ha",
                    "type": "comprehensive",
                    "number": "N21",
                    "Source": "新课标1",
                    "Description": [
                        {
                            "Qu": r"""
                            ### 21. 已知函数 $f(x) = e^x + ax^2 - x$.

(1) 当 $a = 1$ 时, 讨论 $f(x)$ 的单调性;

(2) 当 $x \geq 0$ 时, $f(x) \geq \frac{1}{2} x^3 + 1$, 求 a的取值范围.
                            
"""
                        }
                    ],
                    "An": r"""
                    [答案](1) 当 $x \in (-\infty, 0)$ 时, $f'(x) < 0$, $f(x)$ 单调递减；当 $x \in (0, +\infty)$ 时,
$f'(x) > 0$, $f(x)$ 单调递增. (2) $\left[\frac{7-e^2}{4}, +\infty\right)$
                    """
                },  # 202001,21,ha

        {
            "id": 37,
            "year": 2020,
            "difficulty": "ez",
            "type": "choice" ,
            "number": "N1",
            "Source": "新课2",
            "Description": [
                {
                    "Qu": r"""1. 已知集合 $U=\{-2,-1,0,1,2,3\}, A=\{-1,0,1\}, B=\{1,2\}$, 则 $Q_U(A \cup B)=()$ 

A. {-2, 3}
B. {-2, 2, 3}
C. {-2, -1, 0, 3}
D. {-2, -1, 0, 2, 3}
                    """
                }
            ],
            "An": "A"
        },  # 202002,1,ez
        {
            "id": 38,
            "year": 2020,
            "difficulty": "av",
            "type": "choice" ,
            "number": "N4",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
北京天坛的圜丘坛为古代祭天的场所，分上、中、下三层，上层中心有一块圆形石板(称为
天心石)，环绕天心石砌9块扇面形石板构成第一环，向外每环依次增加9块，下一层的第一环
比上一层的最后一环多9块，向外每环依次也增加9块，已知每层环数相同，且下层比中层多
729块，则三层共有扇面形石板(不含天心石)（ ） 
A. 3699块B. 3474块C. 3402块D. 3339块           
                    """
                }
            ],
            "An": "C"
        },  # 202002,4,av
        {
            "id": 37,
            "year": 2020,
            "difficulty": "me",
            "type": "choice",
            "number": "N10",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
10. 已知 $\triangle ABC$ 是面积为 $9\sqrt{3}$ 的等边三角形, 且其顶点都在球O的球面上. 若球O的表面积为 $16\pi$, 则O到平面ABC的距离为()
A. $\sqrt{3}$ 
B. $\frac{3}{2}$
C. 1
D. $\frac{\sqrt{3}}{2}$
        """
                }
            ],
            "An": "c"
        },  # 202002,10,me
        {
            "id": 38,
            "year": 2020,
            "difficulty": "hard",
            "type": "choice",
            "number": "N12",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
12. 0-1周期序列在通信技术中有着重要应用.若序列 $a_1 a_2 \cdots a_n \cdots$ 满足 $a_i \in \{0,1\}(i=1,2,\cdots)$, 且存在正整数m, 使得 $a_{i+m}=a_i(i=1,2,\cdots)$ 成立,则称其为0-1周期序列,并称满足 $a_{i+m}=a_i(i=1,2,\cdots)$ 的最小正整数 m为这个序列的周期.对于周期为 m的0-1序列 $a_1 a_2 \cdots a_n \cdots, C(k)=\frac{1}{m}\sum_{i=1}^m a_i a_{i+k}(k=1,2,\cdots, m-1)$ 是描述其性质的重要指标,下列周期为5的0-1序列中,满足 $C(k)\leq\frac{1}{5}(k=1,2,3,4)$ 的序列是()
A. 11010.
B. 11011...
C. 10001...
D. 11001…
        """
                }
            ],
            "An": "C"
        },  # 202002,12,ha

        {
            "id": 39,
            "year": 2020,
            "difficulty": "ez",
            "type": "gap",
            "number": "N13",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
                   13. 已知单位向量 a, b的夹角为 $45^{\circ}$, $k a - b$ 与 a垂直,则 $k = $
"""
                }
            ],
            "An": "\\frac{\\sqrt{2}}{2}"
        },  # 202002,13,ez
        {
            "id": 40,
            "year": 2020,
            "difficulty": "av",
            "type": "gap",
            "number": "N14",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu" :r"""
                   .4名同学到3个小区参加垃圾分类宣传活动，每名同学只去1个小区，每个小区至少安排1名
同学，则不同的安排方法共有__________种
                   """
                }
            ],
            "An": r"36"
        },  # 202002,14,av
        {
                    "id": 41,
                    "year": 2020,
                    "difficulty": "me",
                    "type": "gap" ,
                    "number": "N15",
                    "Source": "新课标2",
                    "Description": [
                        {
                            "Qu" : r"""$$15.\text{设复数} z_{1}, z_{2}\text{满足}\left|z_{1}\right|=\left|z_{2}\right|=2,\quad z_{1}+z_{2}=\sqrt{3}+i,\text{则}\left|z_{1}-z_{2}\right|=$$
                            """
                        }
                    ],
                    "An": "2 \\sqrt{2}"
                },  # 202002,15,me
        {
                    "id": 42,
                    "year": 2020,
                    "difficulty": "ha",
                    "type": "gap",
                    "number": "N16",
                    "Source": "新课标2",
                    "Description": [
                        {
                            "Qu" :r"""
                            ### 16. 设有下列四个命题:
$p_1$: 两两相交且不过同一点的三条直线必在同一平面内.
$p_2$: 过空间中任意三点有且仅有一个平面.
$p_3$: 若空间两条直线不相交,则这两条直线平行.
$p_4$: 若直线l平面a，直线m平面a，则ml.
则下述命题中所有真命题的序号是
① $p_1 \wedge p_4$ ② $p_1 \wedge p_2$ ③ $\neg p_2 \vee p_3$ ④ $\neg p_3 \vee \neg p_4$
                            """,
                        }
                    ],
                    "An": "①③④"
                },  # 202002,16,ha

        {
            "id": 43,
            "year": 2020,
            "difficulty": "ez",
            "type": "comprehensive",
            "number": "N17",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
                            ### $$\text{17.} \triangle ABC \text{中,} \sin^2 A - \sin^2 B - \sin^2 C = \sin B \sin C.$$
(1) 求 A;
(2) 若 $BC = 3$, 求 $\triangle ABC$ 周长的最大值.

"""
                }
            ],
            "An": r"""$$\text{答案:}(1) \frac{2\pi}{3}; \quad (2) 3 + 2\sqrt{3}.$$
                    """
        },  # 202002,17,ez
        {
            "id": 44,
            "year": 2020,
            "difficulty": "av",
            "type": "comprehensive",
            "number": "N19",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
                            18. 某沙漠地区经过治理,生态系统得到很大改善,野生动物数量有所增加.为调查该地区某种野生动物的数量,将其分成面积相近的200个地块,从这些地块中用简单随机抽样的方法抽取 20个作为样区,调查得到样本数据 $\left(x_i, y_i\right)(i=1,2,\ldots, 20)$, 其中 $x_i$ 和 $y_i$ 分别表示第 i个样区的植物覆盖面积(单位:公顷)和这种野生动物的数量,并计算得
$$\sum_{i=1}^{20} x_i = 60,$$
$$\sum_{i=1}^{20} y_i = 1200,$$
$$\sum_{i=1}^{20}\left(x_i - \bar{x}\right)^2 = 80,$$
$$\sum_{i=1}^{20}\left(y_i - \bar{y}\right)^2 = 9000,$$
$$\sum_{i=1}^{20}\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right) = 800.$$
(1) 求该地区这种野生动物数量的估计值(这种野生动物数量的估计值等于样区这种野生动物数量的平均数乘以地块数);
(2) 求样本 $\left(x_i, y_i\right)(i=1,2,\ldots, 20)$ 的相关系数(精确到 0.01);
(3) 根据现有统计资料,各地块间植物覆盖面积差异很大.为提高样本的代表性以获得该地区这种野生动物数量更准确的估计,请给出一种你认为更合理的抽样方法,并说明理由.
附: 相关系数 $r = \frac{\sum_{i=1}^n\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)}{\sqrt{\sum_{i=1}^n\left(x_i - \bar{x}\right)^2 \sum_{i=1}^n\left(y_i - \bar{y}\right)^2}}$, $\sqrt{2} = 1.414$.
"""
                }
            ],
            "An": r"""(1)12000；（2）0.94．(3)由于各地块间植物覆盖面积差异较大，为提高样本数据的代表性，应采用分层抽样
先将植物覆盖面积按优中差分成三层，
在各层内按比例抽取样本，
在每层内用简单随机抽样法抽取样本即可
                    """
        },  # 202002,18,av
        {
            "id": 45,
            "year": 2020,
            "difficulty": "me",
            "type": "comprehensive",
            "number": "N20",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
                    19. 已知椭圆 $C_1: \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ (a > b > 0) 的右焦点 F 与抛物线 $C_2$ 的焦点重合, $C_1$ 的中心与 $C_2$ 的顶点重合. 过 F 且与 x轴垂直的直线交 $C_1$ 于 A, B两点,交 $C_2$ 于 C, D两点,且 $|CD| = \frac{4}{3}|AB|$.
(1) 求 $C_1$ 的离心率;
(2) 设 M 是 $C_1$ 与 $C_2$ 的公共点, 若 $|MF| = 5$, 求 $C_1$ 与 $C_2$ 的标准方程.
"""
                }
            ],
            "An": r"""$$(1) \frac{1}{2}; \quad (2) C_{1}: \frac{x^{2}}{36} + \frac{y^{2}}{27} = 1, C_{2}: y^{2} = 12x.$$
            """
        },  # 202002,19,me
        {
            "id": 46,
            "year": 2020,
            "difficulty": "ha",
            "type": "comprehensive",
            "number": "N21",
            "Source": "新课标2",
            "Description": [
                {
                    "Qu": r"""
                           ### 21. 已知函数 $f(x) = \sin^2 x \sin 2x$.
(1) 讨论 $f(x)$ 在区间 $(0, \pi)$ 的单调性;
(2) 证明: $|f(x)| \leq \frac{3\sqrt{3}}{8}$;
(3) 设 $n \in \mathbb{N}^*$, 证明: $\sin^2 x \sin^2 2x \sin^2 4x \ldots \sin^2 2^n x \leq \frac{3^n}{4^n}$.
"""
                }
            ],
            "An": r"""
                    [详解(1)由函数的解析式可得:  $f(x)=2\\sin^3 x\\cos x$  ,则:

$$f'(x)=2\\left(3\\sin^2 x\\cos^2 x-\\sin^4 x\\right)=2\\sin^2 x\\left(3\\cos^2 x-\\sin^2 x\\right)$$
$$=2\\sin^2 x\\left(4\\cos^2 x-1\\right)=2\\sin^2 x(2\\cos x+1)(2\\cos x-1),$$
$$f'(x)=0\\text{在} x\\in(0,\\pi)\\text{上的根为:} x_1=\\frac{\\pi}{3}, x_2=\\frac{2\\pi}{3},$$

当  $x\\in\\left(0,\\frac{\\pi}{3}\\right)$  时,  $f'(x)>0, f(x)$  单调递增,

当  $x\\in\\left(\\frac{\\pi}{3},\\frac{2\\pi}{3}\\right)$  时,  $f'(x)<0, f(x)$  单调递减,

当  $x\\in\\left(\\frac{2\\pi}{3},\\pi\\right)$  时,  $f'(x)>0, f(x)$  单调递增.

(2)注意到  $f(x+\\pi)=\\sin^2(x+\\pi)\\sin[2(x+\\pi)]=\\sin^2 x\\sin 2 x=f(x)$  .

故函数  $f(x)$  是周期为  $\\pi$  的函数.

结合(1)的结论,计算可得:  $f(0)=f(\\pi)=0$  ,

$$ f\\left(\\frac{\\pi}{3}\\right)=\\left(\\frac{\\sqrt{3}}{2}\\right)^2\\times\\frac{\\sqrt{3}}{2}=\\frac{3\\sqrt{3}}{8}, f\\left(\\frac{2\\pi}{3}\\right)=\\left(\\frac{\\sqrt{3}}{2}\\right)^2\\times\\left(-\\frac{\\sqrt{3}}{2}\\right)=-\\frac{3\\sqrt{3}}{8},$$

据此可得:  $[f(x)]_{\\max}=\\frac{3\\sqrt{3}}{8},[f(x)]_{\\min}=-\\frac{3\\sqrt{3}}{8}$  .

$$\\text{即}|f(x)|\\leq\\frac{3\\sqrt{3}}{8}.$$
(3)结合(2)的结论有:

$$\\sin^2 x\\sin^2 2 x\\sin^2 4 x\\cdots\\sin^2 2^n x$$

$$=\\left[\\sin^3 x\\sin^3 2 x\\sin^3 4 x\\cdots\\sin^3 2^n x\\right]^{\frac{2}{3}}$$
$$\\begin{align*}&=\\left[\\sin x\\left(\\sin^2 x\\sin 2 x\\right)\\left(\\sin^2 2 x\\sin 4 x\\right)\\cdots\\left(\\sin^2 2^{n-1} x\\sin 2^n x\\right)\\sin^2 2^n x\\right]^{\frac{2}{3}}\\end{align*}$$
$$\\begin{align*}&\\sin^2 x\\sin^2 2 x\\sin^2 4 x\\cdots\\sin^2 2^n x\\ =&{\\left[\\sin^3 x\\sin^3 2 x\\sin^3 4 x\\cdots\\sin^3 2^n x\\right]^{\frac{2}{3}}}\\ =&{\\left[\\sin x\\left(\\sin^2 x\\sin 2 x\\right)\\left(\\sin^2 2 x\\sin 4 x\\right)\\cdots\\left(\\sin^2 2^{n-1} x\\sin 2^n x\\right)\\sin^2 2^n x\\right]^{\frac{2}{3}}}\\ \leq&{\\left[\\sin x\\times\\frac{3\\sqrt{3}}{8}\\times\\frac{3\\sqrt{3}}{8}\\times\\cdots\\times\\frac{3\\sqrt{3}}{8}\\times\\sin^2 2^n x\\right]^{\frac{2}{3}}}\\end{align*}$$
$$\\leq\\left[\\left(\\frac{3\\sqrt{3}}{8}\\right)^n\\right]^{\frac{2}{3}}=\\left(\\frac{3}{4}\\right)^n.$$
$$\\begin{align*}&\\leq\\left[\\left(\\frac{3\\sqrt{3}}{8}\\right)^n\\right]^{\frac{2}{3}}=\\left(\\frac{3}{4}\\right)^n.\\end{align*}$$
                    """
        },  # 202002,21,ha




    ]
}

with open('question_data.json', 'w', encoding='utf-8') as f:  # 打开question_data.json文件用于写入操作，with保证一直连续写入
    json.dump(data, f, ensure_ascii=False, indent=4)  # ensure_ascii=False表示输出的JSON字符串可以包含非ASCII字符，且保证格式为缩进为4个字符