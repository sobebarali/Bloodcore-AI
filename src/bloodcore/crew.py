from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


# Uncomment the following line to use an example of a custom tool
# from bloodcore.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# Initialize the tools
search_tool = SerperDevTool()


@CrewBase
class BloodcoreCrew():
	"""Bloodcore crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
 
	@agent
	def blood_test_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['medical_analyst'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
		)

	@agent
	def article_searcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
		)
  
	@agent
	def recommendation_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['health_advisor'],
			verbose=True,
		)

	@task
	def blood_test_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_blood_test_report'],
			agent=self.blood_test_analyzer(),
		)

	@task
	def article_search(self) -> Task:
		return Task(
			config=self.tasks_config['find_relevant_articles'],
			agent=self.article_searcher(),
			output_file='report.md',
		)
  
	@task
	def recommendation_generation(self) -> Task:
		return Task(
			config=self.tasks_config['provide_health_recommendations'],
			agent=self.recommendation_generator(),
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Bloodcore crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)