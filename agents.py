from crewai import Agent
from tools.search_tools import SearchTools


class AINewsLetterAgents():
    def editor_agent(self):
        return Agent(
            role='Editor',
            goal='Oversee the creation of the Hedge Fund Newsletter',
            backstory="""With a keen eye for detail and a passion for storytelling, you ensure that the newsletter
            not only informs but also engages and inspires the readers.""",
            allow_delegation=True,
            verbose=True,
            max_iter=15
        )

    def news_fetcher_agent(self):
        return Agent(
            role='NewsFetcher',
            goal='Fetch the top news stories for the day for the topics of economics, credit, agriculture, and real estate, in Brazil',
            backstory="""As a digital sleuth, you scour the internet for the latest and most impactful developments
            in the world of AI, ensuring that our readers are always in the know. You currently work for a brazillian hedge fund
            with interests in economics, credit, agriculture, and real estate.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and generate a detailed markdown summary',
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            analyses of news stories in the topics of economics, credit, agriculture, and real estate, making them accessible
            and engaging for our audience, which are the employees of a Brazillian hedge fund with a vested interest in
            these topics.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def newsletter_compiler_agent(self):
        return Agent(
            role='NewsletterCompiler',
            goal='Compile the analyzed news stories into a final newsletter format',
            backstory="""As the final architect of the newsletter, you meticulously arrange and format the content,
            ensuring a coherent and visually appealing presentation that captivates our readers. Make sure to follow
            newsletter format guidelines and maintain consistency throughout.""",
            verbose=True,
        )
