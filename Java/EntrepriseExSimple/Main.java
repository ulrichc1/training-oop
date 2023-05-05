public class Main {
    public static void main(String[] args){
        Entreprise E1 = new Entreprise("Entreprise 1");
        Groupe G1 = new Groupe("Groupe 1");
        Groupe G2 = new Groupe("Groupe 2");
        Contact Dupont = new Contact("Dupont", "75005 Paris", "0123456789", "dupont@xyz.com");
        Contact Durand = new Contact("Durand", "75006 Paris", "0111111111", "durand@xyz.com");
        Contact Martin = new Contact("Martin", "75007 Paris", "0123451229", "martin@xyz.com");
        Contact Dupuis = new Contact("Dupuis", "75008 Paris", "0785858528", "dupuis@gmail.com");
        Contact Dubois = new Contact("Dubois", "75009 Paris", "0156832589", "dubois@yahoo.fr");

        E1.ajouterGroupe(G1);
        E1.ajouterGroupe(G2);
        G1.ajouterContact(Dupont);
        G1.ajouterContact(Durand);
        G2.ajouterContact(Martin);
        G2.ajouterContact(Dupuis);
        G2.ajouterContact(Dupont);
        G1.ajouterContact(Dubois);

        System.out.println(E1);


        System.out.println("Suppression du contact Dupont du groupe G1");
        G1.supprimerContact(Dupont);
        System.out.println(G1);

        System.out.println("Suppression du groupe G2 de l'entreprise E1");
        E1.supprimerGroupe(G2);
        System.out.println(E1);

        System.out.println("Modification du nom du groupe G1");
        G1.setNom("Groupe 1 bis");
        System.out.println(G1);

        System.out.println("Modification du nom de l'entreprise E1");
        E1.setNom("Entreprise 1 bis");
        System.out.println(E1);

        System.out.println("Ajout du contact Martin dans le groupe G1");
        G1.ajouterContact(Martin);
        System.out.println(G1);

        // Affichage des groupes de l'entreprise E1
        System.out.print("Groupes de l'entreprise E1: ");
        for (Groupe groupe : E1.getGroupes()) {
            System.out.print(groupe.getNom() + " ");
        };
    }
}
