#libraries
#Naturallanguageprocessing
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
#networkx&matplotlib
import networkx as nx
import pylab as plt
ArticlesPS="""
Is this another joke or hyperbole?
President Duterte vowed yesterday that corrupt officials would suffer the same fate as kidnap suspects he claimed to have thrown off a helicopter in mid-flight when he was mayor of Davao City.
Duterte made reference on how he dealt with criminals in the past to drive a point that he is serious about his government’s anti-corruption drive.</articleproper>
“If you are corrupt I will fetch you with a helicopter and I will throw you out on the way to Manila,” he said in Filipino yesterday in a speech at the Camarines Sur provincial capitol after he visited disaster-stricken areas affected by Typhoon Nina.
“I have done that before, why should I not do it again?” said Duterte after he announced that he was giving between P50 million to P100 million in financial assistance for disaster-stricken areas, in addition to a standby P1-billion calamity fund.
Duterte stressed that his anti-corruption drive, like his anti-drug campaign, will remain the main focus of his six-year term.
He has already gotten flak from international human rights groups over summary executions and his recent admission that he personally hunted criminals and killed them when he was Davao mayor.
Duterte narrated an incident when he had to go after kidnappers of a Chinese who mercilessly abused their victim even after the parents paid ransom.
Duterte recalled ordering the pilot to fly at the proper height, indicating the helicopter must be at the right distance from the ground so the body’s splatter won’t cause a commotion.
‘Take it or leave it’
Duterte offered no apologies for his harsh language, which had in the past triggered outrage from US President Barack Obama, members of the United Nations and the European Union. He said it is just the way he speaks. “I am that person, take it or leave,” he said.
In a previous interview during the campaign, Duterte admitted killing three kidnap suspects during an encounter.
He cited also a Chinese kidnap victim was involved in that operation which happened in 1988.  
There was a report of Duterte killing a drug dealer by dropping him off a helicopter when he was mayor, but it is not clear whether the President was referring to this incident in yesterday’s speech.
In the same speech, Duterte even mentioned in passing that he did not spare two of his fraternity brothers for accepting P50-million bribe from a Macau-based online gambling operator of the Fontana Leisure Parks and Casino in Pampanga.  
After announcing his assistance to the disaster victims, Duterte reiterated anew his seriousness in the anti-drug campaign.
This time, Duterte said he is faced with a tough problem on how to deal with four million drug users.
“Out of the four million, at a liberal computation, just give me one million who had gone crazy. What will I do with them? Turn them into fertilizer? I can do that in Mindanao, but here you’ll just report it. But that’s our problem,” he said. In criminal lingo, only rotten bodies turn up as fertilizers.
Duterte also slammed the Catholic Church for criticizing him over the extrajudicial killings attributed to his brutal campaign against illegal drugs.
He said he believes there is a God, he believes in Allah, but that he does not believe in religion, particularly the Catholic Church.
“My statement’s full of sarcasm because they (priests) have been criticizing me,” the President told the gathering of Davao City barangay captains and kagawads last night.
Duterte said he does not intend to follow any religious practice once he dies. “Cremate me within 24 hours when I die,” he said.

LAOAG CITY (UPDATED 9:11 a.m., February 23) — Presidential bet Rodrigo Duterte said if he is elected president and fails to stop criminality in three months, he will resign and give the presidency to Sen. Ferdinand Marcos Jr.
The tough-talking mayor made the statement during his visit at the Mariano Marcos State University in Batac City on Friday.
“If elected president, give me about three to six months I will get rid of corruption, drugs and criminality,” Duterte said.
However, he admitted that he needs everyone’s cooperation in order to achieve this goal.
“They say my timeline is ambitious, you know if I am already president, in the third month I am sitting there as president and I fail because nobody believes me, I really cannot do it even if you give me 10 years of rule.
“Eh mabuti magsibat na lang kayo, or ako. Kung hindi ko magawa 'yan sa tatlong buwan e 'di ibigay ko na lang kay Bongbong (If I fail in three months, better leave the country or I will step down and give the presidency to Bongbong),” Duterte said.
Duterte added that he has a bond with Bongbong because during the term of President Ferdinand Marcos, Duterte’s father was a member of the cabinet as the secretary of general services.
He described his father as a true “Marcos boy.”
“When Marcos first run for president, all Mindanao governors that time jumped to Liberal Party except two—(former Zamboanga del Sur) Governor (Bienvenido) Ebarle and my father (Vicente Duterte) who stood by Marcos all the way,” Duterte said.
“Speaking of loyalty and friendship, I am proud to say that my father was a close ally of President Marcos until his death,” he added.
Hero's burial
If elected president, Duterte said he will allow the remains of President Marcos to be buried at the Libingan ng mga Bayani.
He said President Marcos was still the best president the country has ever had.
“In hindsight now, looking at the horizon of political deludes he was still the best and the brightest. I can say that because I was around (during the Marcos years),” Duterte said.
He also said that his template of governance is Ferdinand Marcos's, usng the military and police in solving criminality.
“He never hesitated really to use the forces of government to get what he really wanted to do to govern the country,” he said.
Duterte described the Philippines as "clean" during the first years of Martial Law.
He also said that he will impose death penalty by hangin for drugs and all serious offenses connected with drugs.
“I have no choice but to do it,” he said.


LAOAG CITY (UPDATED 9:11 a.m., February 23) — Presidential bet Rodrigo Duterte said if he is elected president and fails to stop criminality in three months, he will resign and give the presidency to Sen. Ferdinand Marcos Jr.
The tough-talking mayor made the statement during his visit at the Mariano Marcos State University in Batac City on Friday.
“If elected president, give me about three to six months I will get rid of corruption, drugs and criminality,” Duterte said.
However, he admitted that he needs everyone’s cooperation in order to achieve this goal.
“They say my timeline is ambitious, you know if I am already president, in the third month I am sitting there as president and I fail because nobody believes me, I really cannot do it even if you give me 10 years of rule.
“Eh mabuti magsibat na lang kayo, or ako. Kung hindi ko magawa 'yan sa tatlong buwan e 'di ibigay ko na lang kay Bongbong (If I fail in three months, better leave the country or I will step down and give the presidency to Bongbong),” Duterte said.
Duterte added that he has a bond with Bongbong because during the term of President Ferdinand Marcos, Duterte’s father was a member of the cabinet as the secretary of general services.
He described his father as a true “Marcos boy.”
“When Marcos first run for president, all Mindanao governors that time jumped to Liberal Party except two—(former Zamboanga del Sur) Governor (Bienvenido) Ebarle and my father (Vicente Duterte) who stood by Marcos all the way,” Duterte said.
“Speaking of loyalty and friendship, I am proud to say that my father was a close ally of President Marcos until his death,” he added.
Hero's burial
If elected president, Duterte said he will allow the remains of President Marcos to be buried at the Libingan ng mga Bayani.
He said President Marcos was still the best president the country has ever had.
“In hindsight now, looking at the horizon of political deludes he was still the best and the brightest. I can say that because I was around (during the Marcos years),” Duterte said.
He also said that his template of governance is Ferdinand Marcos's, usng the military and police in solving criminality.
“He never hesitated really to use the forces of government to get what he really wanted to do to govern the country,” he said.
Duterte described the Philippines as "clean" during the first years of Martial Law.
He also said that he will impose death penalty by hangin for drugs and all serious offenses connected with drugs.
“I have no choice but to do it,” he said.


MANILA, Philippines — President Rodrigo Duterte lashed out at his critics who had been comparing him to Germany's Adolf Hitler.
The president called out the United Nations (UN), European Union (EU) and the United States (US) anew for criticizing his anti-drugs campaign in the country.
"Kaya kung ikaw nandito bakit hindi ka magmumura? (So if you are here, why wouldn't you curse?) You're portrayed or pictured to be some cousin of Hitler and yet do not even bother to find out, to investigate," Duterte said in his speech after arriving from Vietnam early Friday
The president noted that Hitler killed three million Jews but said he is also willing to take down three million drug users to solve the drug issue in the Philippines.
"Hitler massacred three million Jews. Now, there are three million drug addicts. I'd be happy to slaughter them" Duterte said.
"At least if Germany had Hitler the Philippines would have... you know my victims, I would like to be all criminals to finish the problem of my country and save the next generation from perdition," the president added.
Duterte stressed that not a single case was filed against him when the Commission on Human Rights was looking into his alleged links with the Davao Death Squad during his term as mayor.
The international community has been criticizing Duterte's drug war due to the spate of extrajudicial and vigilante killings of drug suspects.
"Okay lang sa akin, sanay ako sa pulitika. Lahat ng kababuyan dumating na sa aking buhay. Pero itong mga ganito... look kayong US, EU you can call me anything but I was never into or I am never into hypocrisy like you," Duterte said.
The chief executive argued that both the EU and the US have closed its doors to migrants from the Middle East.
"There are migrants escaping from the Middle East. You allow them to rot and then you're worried about the deaths of about one thousand, or two thousand, or three thousand," the president said.
Duterte earlier said that he is willing to face investigation by the UN, the US and the EU over the killings of drug suspects as long as they follow Philippine laws.


MANILA, Philippines — President Rodrigo Duterte on Wednesday stressed that he does not have plans to declare martial law in the country but added that he would stay quiet if he decides to do so.
"I will not declare martial law at kung mag-declare ako ng Martial Law hindi ako mag-iingay," Duterte said in a speech in Cabanatuan City, Nueva Ecija.
The president cited a military report that there is no compelling reason to impose martial rule in the country at this moment.
"If I feel as a president that I have to preserve my country, I will declare martial law," the president said.
Duterte noted the provisions in the 1987 Constitution which allow any Filipino citizen to file a petition before the Supreme Court to question the basis for declaring martial law.
The president said that the framers of the 1987 Constitution "destroyed" the provisions in connection to martial law because of their "hatred" for ousted dictator Ferdinand Marcos.
"In the same paragraph, the president after 60 days should go to Congress for an extension if wants to... complete the slaughter. Ngayon pagdating sa Supreme Court, sabihin ng Supreme Court it is baseless, it does not amount to any legal basis, sabihin ng Congress go ahead because it is the national security which is at stake," Duterte said.
Different opinions coming from the Congress and the Supreme Court, both co-equal branches of the government, may produce a dilemma for the chief executive.
"Who decides now? Supreme Court sabi 'wag. Congress said yes. Who decides? It is the president so ako. It will discourage me to become a despot because I now can interpret the law itself and it is final," Duterte said.
A few days ago, Duterte said that he would declare martial law if the drug problem in the country becomes virulent. His communications chief then griped about the media's reporting on the president's statement.
Some senators have warned the president to stop making threats on martial law.
Duterte has repeatedly toyed with the idea of martial law in his speeches, at times dismissing the need for it while on certain occasions announcing his apparent intention to use it to fight the drug menace


MANILA, Philippines — President Rodrigo Duterte claimed on Sunday that a Chinese official has suggested that he align himself with China because the Philippines cannot expect anything from the United States.
“Ito namang China sabi niya, ‘lumipat ka na sa amin wala kayong makukuha diyan (Shift your alliance to us. You won’t gain anything from them),” Duterte said during the opening of the MassKara Festival in Bacolod City.
“I’m going to China to make friends with them and also with Russia,” he added.
Duterte did not identify the Chinese official he was quoting. Before making the remark, the president was talking about his meeting with Russia Prime Minister Dmitry Medvedev on the sidelines of the Association of Southeast Asian Nations meet in Laos last month. 
Chinese Premier Li Keqiang was present during the ASEAN meet but it was unclear whether he was the Chinese official Duterte was referring to.
The president said he had confided to Medvedev that he was being criticized by the US because of his crackdown on illegal drugs.
“I met with Medvedev. I’m revealing it to you now. Nakiusap ako na ganito ang sitwasyon. Pinahihirapan ako nito at binababoy ako ng mga walanghiya (I told him that the situation was like this. They are making it hard for me and they are shamelessly bastardizing me),” Duterte said.
“Sabi niya ganun talaga Amerika, so istorya kami. ‘Sige tulungan ka namin,’ (He said America is like that. We will help you),” he added.
'Putin, Xi will be my close friends'
Duterte reiterated that he would seek stronger ties with China and Russia, countries widely perceived to be rivals of the US.
“Tomorrow, (Russia president Vladimir) Putin and (China president) Xi Jinping will be my close friends,” he said in jest.
The Philippine leader said he is not afraid if his policy pronouncements would turn off US investors.
“You said you would take away your dollars. Go ahead take them away,” he added.
The US has not said that it would do that. Last month, credit rating firm Standard and Poor's retained its credit rating of the Philippines of 'BBB', a notch above investment grade with a ‘stable’ outlook. It also noted, however, that there are "rising uncertainties surrounding the stability, predictability, and accountability of [the Philippines'] new government." 
He has previously said that he can go to China and Russia for investments and alliances. He said are "waiting" for him.
The US, a long-time ally and treaty partner of the Philippines, has called out the Duterte administration for the alleged extrajudicial killings linked to the government’s anti-drug war.
The remarks drew the ire of Duterte who viewed them as undue interference with the Philippines’ internal affairs.
The president has threatened to put an end to joint military exercises of Filipino and American troops within his term. He has also bared plans to review the Enhanced Defense Cooperation Agreement (EDCA), a 2014 deal that grants Americans access to Philippine military bases.
Despite his tough talk, Duterte had said he would not cut ties with the US.
“We are not going to cut our umbilical cord with the countries we are allied with,” Duterte said last month.
“But certainly, we will follow an independent posture and independent foreign policy.”
Duterte admitted though that Filipinos may have to sacrifice once the dynamics of the relationship between the Philippines and the US change. 
“I am asking the Filipino in the coming days, kung totohanin talaga ng Amerika, I’m going to ask you to sacrifice a little bit, but by next year, I would have entered alliances with so many countries,” Duterte said in a speech in Pampanga last Sept. 27. 


MANILA, Philippines -- Days before leaving for a state visit to China, President Rodrigo Duterte said Monday he would set aside the Panatag (Scarborough) Shoal issue for now but vowed to ask the Chinese government to allow Filipino fishermen to go to the area.
Duterte is scheduled to visit China from Oct. 18 to 21 to strengthen the ties between Manila and Beijing, which has been strained by the West Philippine Sea (South China Sea) dispute.
The four-day state visit will come as Duterte is seeking to broaden alliances with China and Russia while engaging in a spat with the United States over his bloody war on illegal drugs.  
“Pupunta ako ng China. Okay tayo sa kanila. Huwag muna nating pakialaman yung Scarborough. Di natin kaya. Magalit man tayo, hangin lang (I will go to China. We are okay with them. Let’s not dwell on the Scarborough issue for now. We can’t solve it even if we get angry),” Duterte said during an agrarian reform forum in Lamitan, Basilan.
“We will ask them to allow our fishermen brothers to return (to the shoal),” he added.
Duterte is optimistic about his talks with the Chinse government, noting that it has already allowed the Philippines to export bananas and pineapple to China.
“I suspect that they really want to help us,” the president said.
Panatag Shoal is located 124 nautical miles from the nearest point in Zambales, well within the Philippines’ exclusive economic zone.
China started occupying the shoal in 2012 after Chinese surveillance ships barred a Philippine Navy vessel from apprehending Chinese fishermen who had poached endangered species. 
China has since maintained its presence in the shoal, barring Filipino fishermen from entering the traditional fishing route.
Last month, the National Security Council reported that Chinese Coast Guard vessels had harassed Filipino fishermen in Panatag Shoal despite calls by Duterte for China to allow entry in the area.
Foreign Affairs secretary Perfecto Yasay Jr. said in an earlier interview that the Philippines would use “quiet diplomacy” to address the issue.
Duterte has repeatedly said that he would not go to war with China over the maritime row because it would result in a “massacre’ of Philippine troops.
A Hague-based arbitral tribunal ruled in July that China’s expansive claim in the South China Sea has no legal basis. The claim, which covers virtually the entire South China Sea, including Panatag Shoal, is being contested by the Philippines, Vietnam, Malaysia, Brunei and Taiwan. The court ruled that the Philippines has sovereign rights over the Panganiban (Mischief) Reef, Ayungin (Second Thomas) Shoal, and Recto (Reed) Bank, areas located off Palawan that are also being claimed by China.
Although the tribunal said it was not ruling on the sovereignty over the Panatag Shoal, it found that China had violated its duty to respect the traditional fishing rights of Filipinos by halting access to the shoal in 2012.
Given that the issue of sovereignty over the shoal has yet to be solved, the Philippine government said that whoever owns those rocks has sovereignty or rights of “full ownership” over them including their territorial sea.
Solicitor General Jose Calida said last August that the implication of the court’s ruling is that the waters immediately beyond the territorial sea around Panatag Shoal are part of the Philippines’ EEZ.
He said the Philippines has “sovereign rights” to explore, exploit, converge and manage the natural resources in its EEZ.



How can the Catholic clergy understand the seriousness of the drug problem? They should try shabu.
A joking President Duterte floated the proposal here on Wednesday as scored the Church anew for its supposed hypocrisy and pretensions.
The Roman Catholic Church, the faith of more than 80 percent of Filipinos, has been vocal in expressing concerns over the spate of killings linked to Duterte's brutal war on drugs. More than 6,000 suspected drug offenders have been killed since Duterte assumed the presidency.Some churches even displayed tarpaulins that read "Thou shall not kill," an obvious reference to the alleged extrajudicial killings happening under the administration.
Duterte, who has repeatedly denied that the government is endorsing summary executions, said he cannot understand why the Church keeps on hitting on his anti-drug war.
"I really cannot understand the Church. They know, their parish priests know how serious it (drug problem) is. And yet they say that's 'extra-judicial killing.' You know that if a person is high on drugs, he will fight (with the authorities)," the president said during the 20th anniversary of the Premiere Medical Center here.
"Kaya dapat 'yung ibang pari, mag-shabu para maintindihan nila (Some priests should take shabu so they would understand). I recommend one or two of the bishops," he added, drawing laughs from the audience.
Duterte then issued sweeping statements about Catholic clergy's supposed illicit affairs and homosexual acts.
"Eh sa kanila walang shabu pero asawa meron. Pareho man kami. Ako pati ang mga pari namin sa Davao? Ah pareho. Tag-dalawa, tatlong asawa. Asus (They don't have shabu but they have wives. We are the same. Even the priests in Davao. Each of them have two or three wives)… All the hypocrisy of, pretension," he said.
"When you expose the frailties of your faithful, you are free to shout on the pulpit but you are exempted. What kind of system is that?"
The Catholic Church has said that there is still hope for drug addicts and that the government should help them recover from their vices. Some Catholic organizations and parishes have launched initiatives seeking to rehabilitate drug users and make them productive members of society.
Duterte has repeatedly said that he is ready to kill drug lords who destroy the country and the next generation even if it costs him his life, his honor and the presidency.
He reiterated that his bloody campaign would not stop until the last drug pusher is out of the streets.
"Kaya mga drug lord dito, panahon lang 'yan, panahon lang. Pangdagdag sa greenery sa mga memorial ninyo dito (For the drug lords, it's just a matter of time. They can be added to the greenery of your memorial parks here)," the president said.


MANILA, Philippines – President Duterte scored the United Nations yesterday for hitting his aggressive anti-drug campaign, which he said has so far claimed the lives of 1,000 drug addicts and pushers.
He complained that the UN is zeroing in on his administration’s drug campaign when it was quiet on mass killings in other countries. 
“While I really do not know who’s going to come here for that, I am going to whack him in the head,” Duterte said at the anniversary of the Philippine National Police at Camp Crame.
“Do not investigate us as if we are criminals. Don’t ever do that… I will not receive you warmly in this country. But if you come here, explain or maybe hear about the happenings on criminals or see (for) yourselves,” he said, referring to UN probers.
He accused the UN of interfering in the government’s affairs as he urged policemen “not to be intimidated about the statement of the United Nations.”
“UN can only investigate genocide, when you kill… killing children, killing the whole community… but when you kill criminals who fight you and criminals who fight among themselves, that is our duty.”
“We will answer for every killing that involves a human being, whether it is connected with the fulfillment of duty of the police or not,” he said.
He said many people  have lost their sons and daughters to drugs and have been waiting for this time to seek justice. 
He also described as “stupid” the reports accusing the government of being behind all the summary executions.
“Here comes the UN easily swayed and coming on a very stupid proposition of, you know, for those who are killed by the drug syndicates we can only investigate, but do not attribute acts of other criminals upon my government,” he said.
“I would like also to just say why would the United Nations be so easily swayed into interfering in the affairs of this republic?” he asked.
“There are about just 1,000. There are a lot of people, innocent women, child, young women, young men, old men, old women being killed elsewhere in this world without ever seeing the slightest justice.”
Suicide bombings
Duterte cited for example in the Middle East, where there have been lives lost due to suicide bombings.
“I have yet to see the United Nations complaining publicly, even not criticizing countries who are into bombing villages and communities, killing everybody there including the goats and the cows and the dogs,” Duterte said.
Shoot them dead
Amid international outcry over human rights violations, Duterte reiterated his call to the police to kill drug suspects who will resist during operations.
“I will suppress crime and take control of the drug situation, which was really running wild. Make no mistake about it,” he said.
“Do not hesitate to kill if you are in danger of losing your life,” he told policemen.
“If you cannot bring him to the police station… (and you need) to overcome the resistance... and in the process the operation is placing your life in jeopardy – shoot and shoot him dead.”
Duterte said it is very easy to complain when no president had earlier made a successful, honest-to-goodness policy to really stomp out the drug menace in the country.
“We in government and I myself who ordered the campaign against drugs, take full sole responsibility for it and for those who are killed in a police operation and a firefight, we are willing to submit ourselves for an investigation before anybody.”
Duterte downplayed the statistics on the victims of killings, saying he is saving the nation from the peril posed by illegal drugs. 
He said the numbers are small compared to the lives wasted by drugs, which create broken families, and the root of heinous crimes such as rape, robbery and murder.
But despite intensive effort to contain illegal drugs, the menace remains rampant in the National Capital Region, Bicol and Western Visayas.
100 more SAF at NBP
At the New Bilibid Prison in Muntinlupa City, at least 100 more members of the elite Special Action Force of the PNP will be deployed on top of around 320 SAF members that have taken over the prison security since last July 20.
Justice Secretary Vitaliano Aguirre II said the additional 100 SAF troopers were earlier requested to augment the 320 already deployed there last month. 
Aguirre said the deployment of 100 more SAF would be funded by the Department of Justice, with the Bureau of Corrections as one of 11 agencies under its wing. 
He also cited the need for signal jammers in the NBP to prevent transactions of illegal drugs from taking place between the inmates and their connections outside the penitentiary. 
“We have to replace the signal jammers and we are looking for donors who could buy the one worth P10 million that has to be bought from Israel,” he said during a press conference on the sidelines of the Social Development Summit at the SMX Convention Center.



MANILA, Philippines (Updated 9:29 p.m.) – President Rodrigo Duterte on Thursday announced that he is cutting ties with the United States, the Philippines' long-time ally and trading partner.
In a 40-minute long speech peppered with expletives, Duterte said the US has been arrogant and has been imposing its policies on other countries, including the Philippines, its traditional partner and treaty ally.
"In this venue, I announce my separation from the United States both in the military…not social, but economics also,” Duterte said, earning a standing ovation from businessmen during the Philippines-China Trade and Investment Forum.
"I have separated from them so I will be dependent on you (China) for a long time but don't worry we will also help," he added.
The relations between the Philippines and the US has had a rough sailing since Duterte assumed the presidency last July. The tough-talking president accused the US of insulting him after American officials had raised concerns over the alleged extrajudicial killing of drug suspects in the Philippines
Early this month, Duterte said he would no longer allow the military to conduct joint military drills with American troops, activities that are part of a decades-old defense treaty signed by the two countries.
He clarified then that he was not severing ties with the US but was merely implementing an independent foreign policy.
The president is known for makings statements that he later retracts or that his spokespersons later clarify.
Previously, Foreign Affairs Secretary Perfecto Yasay and Chief Legal Presidential Counsel Salvador Panelo clarified that Duterte’s pronouncement of “crossing the Rubicon with the US” did not mean cutting ties with the country’s former colonizer.
Presidential Spokesperson Ernesto Abella has also said that Duterte's statements are not policy until official action is taken.
Economic managers: We will maintain relations with the West
Duterte’s economic managers said Duterte’s policy would open the Philippines to trade and investment opportunities in the region.
“The president just gave a very important speech. The Cabinet will move strongly and swiftly towards regional economic integration. This is why the president prioritized foreign trips to ASEAN (Association of Southeast Asian Nations) and Asia,” Finance Secretary Carlos Dominguez and Socioeconomic Planning Secretary Ernesto Pernia said in a joint statement.
“As a result, the Philippines has now opened its opportunities for trade and investment to a market of 1.8 billion people across the region. ASEAN economies have expressed interest in integration. China has committed to open its capital markets,” they added.
 “We will maintain relations with the West but we desire stronger integration with our neighbors. We share the culture and a better understanding with our region."
Pernia and Dominguez said the Philippines is integrating with ASEAN and East Asian countries China, Japan and South Korea.
“In a way, Asian economic integration is long overdue compared with the regional economic integrations,” they said.
Aside from Asian countries, the Philippines is also seeking closer ties with Russia.
"I realign myself in your ideological flow and maybe I will also go to Russia to talk to (Russia President Vladimir) Putin. There are three of us against the world. China, Philippines, Russia," Duterte said.
In the same event, Duterte praised China for being sincere and for not being arrogant, traits that he said are typical of Orientals, an outdated and sometimes offensive term for East Asians



MANILA, Philippines — President-elect Rodrigo Duterte is unfazed by reports that drug lords have placed a bounty on his head and even promised higher sums and promotion to policemen who will “slaughter” those who are involved in the narcotics trade.
Duterte, who has vowed to wage a bloody war against criminality, said he is ready to match the bounty offered for his life.
“If he (drug lord) puts P50 million for my life, I will put P60 million. Kill him. No questions asked. We can match each other’s price,” Duterte said during the turnover ceremony of the Davao City Police Office Friday.
“If he puts up P100 million, I will give you P150 million. Slaughter them and I will be happy,” he added.
In jest, Duterte promised to give an on-the-spot promotion to policemen who would eliminate drug lords.
“I will give you a promotion on the spot from PO1 to general,” he said.
Duterte reiterated that policemen can kill criminals if they do so to defend themselves.
“These are my orders and listen very carefully. If you encounter a criminal ask him to surrender. If he chooses to fight and you think, you feel in your guts that you will die in the fighting, unahan mo na (go ahead). Kill the criminal especially those involved in drugs,” he said.
Government officials not spared
Duterte said mayors with links to drug syndicates would not be spared from his anti-narcotics campaign.
“Let’s not fool each other. Your (policemen) job is to guard him (mayor with links to drug syndicates). Find the truth and if he is arrested and chooses to fight you kill him,” the tough-talking leader said.
Duterte said he would ask Congress to amend the law allowing mayors to assign police chiefs in their area.
“The national government will do it. Why? Many who are into drugs won as mayor of their respective towns and cities. I won’t give them that luxury,” he said.
Duterte, nevertheless, reminded policemen to follow existing laws in performing their operations.
“Just stick to the rules and tell me the truth. Do not lie to me. I will take charge,” he said.
“It is not taught in criminal books that you can shoot people who are tied,” he added.
Duterte also advised policemen not to be afraid to perform their duties.  
“Do not die. Kill the criminal. I will even give you a medal as big as a plate,” he said.
The incoming president, however, stressed that law enforcers’ loyalty should be directed to the country and the constitution and not to him.
“Do not nurture loyalty to me. I don’t need it I don’t need adulation. All that I ask of you is do your duty according to the law,” Duterte said.
Duterte promised to double the salaries of policemen by the end of the year. He also vowed to put up a fund for policemen who need financial assistance.





"""





#tokenizer
lemmatizer=WordNetLemmatizer()
G=nx.DiGraph()
wordsArticles = word_tokenize(ArticlesPS)
stop_words =set(stopwords.words("english"))
tokenize = []
counter=0
label=""
#print(wordsarticle)
for i in wordsArticles:
    if i not in stop_words:
        tokenize.append(lemmatizer.lemmatize(i))
        
for j in range(0,len(tokenize)):
    G.add_node(j, value = tokenize[j])
    
G2 = G.copy()
for u1,v1 in G.nodes(data=True):
    WeightC=0
    for u2, v2 in G2.nodes(data=True):
        if(v1['value'] == v2['value'] and u1 != u2):
            WeightC= WeightC + 1 
            G.add_edge(u1,u2,weight=WeightC)
    
nx.write_gexf(G,"Philstar.gexf")
plt.axis('off')
plt.savefig("weighted_graph.png")
nx.draw(G)
plt.show()

