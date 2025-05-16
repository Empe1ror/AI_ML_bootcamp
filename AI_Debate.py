from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate


load_dotenv()

print("---AI Debate---")
topic = input("Please enter your debate topic: ")

def support(topic):

    model1 = ChatOpenAI(model="deepseek/deepseek-prover-v2:free", temperature=0.3)

    support_template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a smart AI student in a debate."),
        HumanMessage(content=f"Support the motion which says {topic}")
    ])

    chain = support_template | model1 | StrOutputParser()

    result = chain.invoke({})
    return f"Student in support of the motion: {result}"

def against(topic, support_result):
    model2 = ChatOpenAI(model="qwen/qwen3-0.6b-04-28:free", temperature=0.3)
    against_template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a smart AI student in a debate."),
        HumanMessage(content=f"Support the motion which says {topic}"),
        AIMessage(content= support_result),
        SystemMessage(content="You are a smart AI student in a debate."),
        HumanMessage(content=f"Against the motion which says {topic}")
    ])

    chain2 = against_template | model2 | StrOutputParser()

    against_result = chain2.invoke({})
    return f"Student against the motion: {against_result}"
def judge(topic, support_result, against_result):
    model3 = ChatOpenAI(model="nousresearch/deephermes-3-mistral-24b-preview:free")
    judge_template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a smart AI student in a debate."),
        HumanMessage(content=f"Support the motion which says {topic}"),
        AIMessage(content=support_result),
        SystemMessage(content="You are a smart AI student in a debate."),
        HumanMessage(content=f"Against the motion which says {topic}"),
        AIMessage(content=against_result),
        SystemMessage(content="You are a smart AI judge in a debate."),
        HumanMessage(content=f"judge the debate and declare the winner.")
    ])

    chain3 = judge_template | model3 | StrOutputParser()

    judge_result = chain3.invoke({})
    return f"Judge result: {judge_result}"
support_result = support(topic)
against_result = against(topic, support_result)
judge_result = judge(topic, support_result, against_result)

print(f"\n {support_result}\n")
print(f"\n {against_result}\n")
print(f"\n{judge_result}")