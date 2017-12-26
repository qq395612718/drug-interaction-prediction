package jenatuili;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.List;
import org.apache.jena.ontology.OntModel;
import org.apache.jena.ontology.OntModelSpec;
import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.ResultSet;
import org.apache.jena.query.ResultSetFormatter;
import org.apache.jena.rdf.model.InfModel;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.Statement;
import org.apache.jena.rdf.model.StmtIterator;
import org.apache.jena.reasoner.rulesys.GenericRuleReasoner;
import org.apache.jena.reasoner.rulesys.Rule;
import org.apache.jena.shared.RulesetNotFoundException;
import org.apache.jena.vocabulary.ReasonerVocabulary;



/**
 * @purpose According to ontology documents and rules, to achieve ontology reasoning function
 * 
 * 
 */
public class Reasonerlmpl implements IReasoner {
	
	private InfModel inf = null;

	/**
	 * Get a reasoning interface
	 * @param path
	 * @return
	 * @throws RulesetNotFoundException
	 */
	private GenericRuleReasoner getReasoner(String path) throws RulesetNotFoundException {
		
		List<Rule> rules = Rule.rulesFromURL(path);  //"file:./family/family.rules"
		GenericRuleReasoner reasoner = new GenericRuleReasoner(rules);
		reasoner.setOWLTranslation(true);
		reasoner.setDerivationLogging(true);
		reasoner.setTransitiveClosureCaching(true);
		return reasoner;
		
	}
	
	/**
	 * Get the ontology of reasoning
	 * @param path
	 * @return
	 */
	private OntModel getOntModel(String path) {
		
		Model model = ModelFactory.createDefaultModel();
		model.read(path);  //"file:./family/family.owl"
		OntModel ont = ModelFactory.createOntologyModel(OntModelSpec.OWL_DL_MEM_RDFS_INF,
				model);
		Resource configuration = ont.createResource(); //a new anonymous resource linked to this model
		configuration.addProperty(ReasonerVocabulary.PROPruleMode
				, "hybrid");
		return ont;
		
	}
	
	/**
	 * InfModel is an extension of the regular Model, supporting any related inference capabilities
	 * @param ontPath
	 * @param rulePath
	 * @return
	 */
	public InfModel getInfModel(String rulePath, String ontPath) {
		
		this.inf = ModelFactory.createInfModel(getReasoner(rulePath), getOntModel(ontPath));
		return this.inf;
		
	}
	
	/**
	 * InfModel is an extension of the regular Model, supporting any related inference capabilities
	 * @param model
	 * @param rulePath
	 * @return
	 */
	public InfModel getInfModel(String rulePath, OntModel model) {
		this.inf = ModelFactory.createInfModel(getReasoner(rulePath), model);
		return this.inf;
	}
	
	/**
	 * Print reasoning results
	 * @param a
	 * @param b
	 */
	public void printInferResult(Resource a, Resource b) {
		
		StmtIterator stmtIter = this.inf.listStatements(a, null, b);
		if (!stmtIter.hasNext()) {
			System.out.println("there is no relation between "
				      + a.getLocalName() + " and " + b.getLocalName());
			System.out.println("\n-------------------\n");
		}
		while (stmtIter.hasNext()) {
			Statement s = stmtIter.nextStatement();
			System.out.println("Relation between " + a.getLocalName() + " and "
				      + b.getLocalName() + " is :");
			System.out.println(a.getLocalName() + " "
				      + s.getPredicate().getLocalName() + " " + b.getLocalName());
			System.out.println("\n-------------------\n");
		}
		
	}
	
	public void searchOnto(String queryString) {
		
		Query query = QueryFactory.create(queryString);	  
	    QueryExecution qe = QueryExecutionFactory.create(query, this.inf);
	    ResultSet results = qe.execSelect();
	    try {
			FileOutputStream fos=new FileOutputStream("C:/Users/dell/Desktop/1.txt");
			ResultSetFormatter.out(fos, results, query);
		    
		    qe.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	    
	}
	
}
