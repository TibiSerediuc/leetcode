#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head) {

    struct ListNode *tempNode = head;

    while(tempNode->next != NULL){

        int currentVal = head->val;

        while(head->next->val == currentVal){
            
        }

        head->next = head->next->next;

    }

}

int main(){

    struct ListNode *head;
    struct ListNode *newElement1, *newElement2;

    head->val = 1;
    newElement1->val = 1;
    newElement2->val = 2;
    newElement2->next = NULL;

    head->next = newElement1;
    newElement1->next = newElement2;


    printf("Ana are mere");
    return 0;
}