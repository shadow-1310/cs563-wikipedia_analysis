from refined.inference.processor import Refined
refined = Refined.from_pretrained(model_name='wikipedia_model',
                                  entity_set="wikipedia")
spans = refined.process_text('''Mayor Bill de Blasio’s counsel and chief legal adviser, Maya Wiley, is resigning next month from her City Hall position to become the chairwoman of the Civilian Complaint Review Board, New York City’s independent oversight agency for the Police Department.
The move represents the latest shake-up for the de Blasio administration amid continuing state and federal investigations into the mayor’s fund-raising, and fills a two-month vacancy at the police review board created by the resignation of its chairman, Richard D. Emery, in April.
A civil rights lawyer and advocate for racial and social justice, Ms. Wiley joined the de Blasio administration in early 2014 to focus on legal issues as well as on the mayor’s efforts to address issues of inequality. But over time, Ms. Wiley became discouraged over not being part of Mr. de Blasio’s inner circle and felt cut out of both legal questions and advocacy, according to a person familiar with her thinking. On the former, Mr. de Blasio often relied instead on the city’s corporation counsel and Henry Berger, the mayor’s special counsel; on the latter, he favored his top political aides. The person requested anonymity to discuss private conversations.
More recently, Ms. Wiley was assigned to help craft the administration’s legal response to the state and federal inquiries as well as to requests for the public disclosure of documents, notably emails between Mr. de Blasio and trusted advisers outside the administration.
It was in response to a question from reporters about the withholding of those emails with advisers that Ms. Wiley, defending the practice, described the advisers as “agents of the city” — a designation that appeared novel and resulted in days of unfavorable press coverage.
In a statement on Wednesday, Mr. de Blasio thanked Ms. Wiley for her service and congratulated her on her new role.
The review board investigates allegations of misconduct by officers and makes recommendations for discipline to the Police Department. Its data on the number of complaints, and its investigations of officers, provide an important barometer of police behavior and a politically important one for Mr. de Blasio, a Democrat who campaigned on improving police-community relations.
Mr. Wiley will also take a position at the New School in Manhattan. Her moves were reported by The Wall Street Journal.
The announcement of Ms. Wiley’s departure from City Hall followed that of a recently hired director of social media, Scott Kleinberg, who resigned on Saturday, just eight weeks after being hired to bring greater personality to the Twitter, Facebook and other online accounts associated with the mayor’s office. His resignation was reported by DNA Info.
In a Facebook post that was later removed, Mr. Kleinberg complained of long hours and micromanagement and described his experience with the administration as working with “political hacks plus a boss who just couldn’t get it,” adding, “It was a bad combination for sure.” Mr. Kleinberg declined to comment.
The departures came less than two months after Karen Hinton, the mayor’s top spokeswoman, announced her resignation from the administration. (She stayed in the position until mid-June.)

''')
print(type(spans))
print(spans)
