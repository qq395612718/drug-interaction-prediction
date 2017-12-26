package jenatuili;



import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Resource;


public class test {
	
	
	public static void testQuery() {
		String ruleFile = "C:/Users/dell/Desktop/Jena本体推理/expert/test.rules";
		String ontoFile = "C:/Users/dell/Desktop/Jena本体推理/expert/test0.05-1.owl";
		String queryString = "PREFIX expert:<http://www.owl-ontologies.com/drug_action.owl#> "+ 
		"SELECT ?expert ?subject " +
	    	"WHERE {?expert expert:Interact ?subject} ";
		
		IReasoner famRea = ReasonerFactory.createFamilyReasoner();
		famRea.getInfModel(ruleFile, ontoFile);
		famRea.searchOnto(queryString);
		
		
	}

	public static void main(String[] args) {
		testQuery();
		System.out.println("finish");
 
	}
	
}
