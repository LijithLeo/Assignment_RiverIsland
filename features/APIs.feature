Feature: Validate new Voting

  Scenario:
    Given Protocol Host Version and Authorization are accessible
    When  We request GET method we should be able to get the list of votes
    When We pick the ID from previous response we should be able to fetch the other details
    When We POST new resource it should accept the new vote
    When We GET we should be able to get the newly created resource
    When We DELETED the nedpoint should delete the newly created resource
    Then We should get 404 error trying to GET the deleted resource


